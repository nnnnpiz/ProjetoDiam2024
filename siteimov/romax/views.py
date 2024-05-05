from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy
from .models import Propriedade, Cliente, ESTADOS_CIVIS, MAX_NAME_LEN, NOME_COMPLETO_REGEX_FORMAT, TELEMOVEL_REGEX_FORMAT
from django.contrib.auth.models import User

# Create your views here.
def landing_page(request):
    return render(request, 'romax/landing_page.html',
                      context={'highlighted_properties': [i for i in range(10)]})

def login(request):
    print( request.POST['user-email'], request.POST['password'] )
    #request.POST['user-email']
    #request.POST['password']
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


    #TODO fix that
def pesquisa_avancada(request):
    return render(request, 'romax/pesquisa_avancada.html')

def resultados_pesquisa(request):
    #pesquisa pelo titulo sera based num regex (case insensitive) *titulo*
    pass #TODO

def criar_conta_page(request):
    return render(request, 'romax/criar_conta_page.html', context = {
        'ESTADOS_CIVIS' : ESTADOS_CIVIS,
        'MAX_NAME_LEN' : MAX_NAME_LEN,
        'NOME_COMPLETO_REGEX_FORMAT': NOME_COMPLETO_REGEX_FORMAT,
        'TELEMOVEL_REGEX_FORMAT' : TELEMOVEL_REGEX_FORMAT
    })

def criar_conta(request):
    # TODO page para se nao foi possivel criar conta (failed server-side validation or server error (5xx))



    #TODO server side

    #Criar conta

    user = User.objects.create_user(request.POST['email'],
                                    request.POST['email'],
                                    request.POST['password']
                                    )
    Cliente.objects.create(
        user=user,
        nomeCompleto = request.POST['nome-completo'],
        telemovel = int(request.POST['telemovel']),
        idade = None if 'idade' not in request.POST else int(request.POST['idade']),
        estadoCivil = None if 'Estado-Civil' not in request.POST else request.POST['Estado-Civil'],
        nif = int(request.POST['NIF']),
        cc = request.POST['CC'],
        animais = 'tem-animais' in request.POST,
    )
    return HttpResponseRedirect(reverse('romax:landing_page'))



def informacaopessoal(request):
    return render(request, 'romax/informacao_pessoal.html')