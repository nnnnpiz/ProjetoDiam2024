from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy
from .models import Propriedade, Cliente,PASSWORD_LEN, ESTADOS_CIVIS, MAX_NAME_LEN, NOME_COMPLETO_REGEX_FORMAT, TELEMOVEL_REGEX_FORMAT, NIF_OR_CC_REGEX_FORMAT
from django.contrib.auth.models import User
import re
from django.contrib.auth.decorators import permission_required, login_required
from django.utils import timezone
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


EMAIL_VALIDATION_REGEX='^[a-z._-]+@[a-z]+.[a-z]+$' #TODO Voltar aqui


EMAIL_VALIDATION_REGEX_COMPILE = re.compile(EMAIL_VALIDATION_REGEX)
NOME_COMPLETO_REGEX_FORMAT_COMPILE = re.compile(NOME_COMPLETO_REGEX_FORMAT)
TELEMOVEL_REGEX_FORMAT_COMPILE = re.compile(TELEMOVEL_REGEX_FORMAT)
NIF_OR_CC_REGEX_FORMAT_COMPILE = re.compile(NIF_OR_CC_REGEX_FORMAT)
# Create your views here.

def landing_page(request):
    context = {
        'highlighted_properties': [i for i in range(10)],# TODO change this
        }
    if(request.user.is_authenticated):
        cliente= Cliente.objects.get(user=request.user)
        nomes = cliente.nomeCompleto.split(' ')
        context['Cliente_1_nome']: nomes[0]
        context['Cliente_ultimo_nome']: nomes[-1]
    return render(request, 'romax/landing_page.html', context=context)

def login_view(request):
    if request.method == 'POST':
        if request.POST['user-email'] and request.POST['password'] and 'user-email' in request.POST and 'password' in request.POST: #se username e pass estao preenchidos
            user = authenticate(username=request.POST['user-email'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return HttpResponse(status=200, content=reverse('romax:landing_page'))
            else:
               return HttpResponse('Utilizador nao existe', status=401)
        else:
            return HttpResponse(status=400, content='400 Bad Request. HTTP request deve vir com o email e password para poder fazer login')
    else:
        return HttpResponse(status=400, content='400 Bad Request. HTTP request deve ser POST')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(
        reverse('romax:landing_page')
    )


def propriedade(request, propriedade_id):
    try:
        propriedade = Propriedade.objects.get(pk=propriedade_id)
        return render(request,
        'romax/propriedade.html',
                      context={'propriedade': propriedade}
                      )
    except (KeyError, Propriedade.DoesNotExist):
        return render(request, 'romax/propriedade_notfound.html', context={
        })

def pesquisa_avancada(request):
    ordernar = [ "Preço ascendente", "Preço descendente", "Maior área", "Menor área", "Mais recente", "Mais antigo"]
    return render(request, 'romax/pesquisa_avancada.html', context={
       'ordernar' : zip(range(1,len(ordernar) ),ordernar)
    })

def resultados_pesquisa(request):
    #pesquisa pelo titulo sera based num regex (case insensitive) *titulo*
    pass #TODO

def criar_conta_page(request):
    return render(request, 'romax/criar_conta_page.html', context = {
        'ESTADOS_CIVIS' : ESTADOS_CIVIS,
        'MAX_NAME_LEN' : MAX_NAME_LEN,
        'NOME_COMPLETO_REGEX_FORMAT': NOME_COMPLETO_REGEX_FORMAT,
        'TELEMOVEL_REGEX_FORMAT' : TELEMOVEL_REGEX_FORMAT,
        'NIF_OR_CC_REGEX_FORMAT' : NIF_OR_CC_REGEX_FORMAT,
        'PASSWORD_LEN' : PASSWORD_LEN
    })

def criar_conta(request):
    # TODO page para se nao foi possivel criar conta (failed server-side validation or server error (5xx))

    #Validar o email
    re.fullmatch(EMAIL_VALIDATION_REGEX_COMPILE,request.POST['email'])

    #validar o nome completo
    nome_completo = request.POST['nome-completo']
    len(nome_completo) <= MAX_NAME_LEN
    re.fullmatch(NOME_COMPLETO_REGEX_FORMAT_COMPILE, nome_completo)

    #validar Telemovel
    telemovel = request.POST['telemovel']
    re.fullmatch(TELEMOVEL_REGEX_FORMAT_COMPILE, telemovel)
    telemovel = telemovel.replace(' ', '')

    #Validar idade se Cliente inseriu uma
    if('idade' in request.POST):
        idade = int(request.POST['idade'])

        18 <= idade <=122
        del idade

    #validar Estado Civil e Cliente inseriu um


    #validar password

    #Criar conta
    try:
        if not User.objects.filter(username=request.POST['email']).exists():
            user = User.objects.create_user(request.POST['email'],
                                        request.POST['email'],
                                        request.POST['password']
                                        )
        else:
            return render(request, 'romax/criar_conta_page.html', context={'error_msg': "User ja existe",})
    except:
        pass #Enviar ao user uma resposta de erro (5XX)
    try:
        Cliente.objects.create(
            user=user,
            nomeCompleto =nome_completo,
            telemovel = int(telemovel),
            idade = None if 'idade' not in request.POST else int(request.POST['idade']),
            estadoCivil = None if 'Estado-Civil' not in request.POST else int(request.POST['Estado-Civil']),
            nif = int(request.POST['NIF']),
            cc = request.POST['CC'],
            animais = 'tem-animais' in request.POST,
        )
    except:
        user.delete()
    return HttpResponseRedirect(reverse('romax:landing_page'))



def informacaopessoal(request):
    return render(request, 'romax/informacao_pessoal.html')