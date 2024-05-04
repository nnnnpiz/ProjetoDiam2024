from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import Propriedade
from romax.models import ESTADOS_CIVIS

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
        prop = Propriedade.objects.get(pk=propriedade_id)
        return render(request, 'romax/propriedade.html', context={
                'propriedade': prop
            }
        )
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
        'ESTADOS_CIVIS' : ESTADOS_CIVIS
    })

def criar_conta(request):
    # TODO page para se nao foi possivel criar conta (failed server-side validation or server error (5xx))

    #TODO tirar antes de delivery
    s='#'*10 + '\n'
    print(s*3)
    print(request.POST)
    print(s*3)

    #TODO server side validation
    user = User.objects.create_user(request.POST['email'],
                                    request.POST['email'],
                                    request.POST['password']
                                    )


    Cliente.objects.create(
        user= user,
        nomeCompleto = request.POST['nome-completo'],
        telemovel = int(request.POST['telemovel']),
        idade = None if 'idade' in request.POST else int(request.POST['idade']),
        estadoCivil = None if 'idade' in request.POST else request.POST['Estado-Civil'],
        nif = int(request.POST['NIF']),
        cc = request.POST['CC'],
        animais = 'tem-animais' in request.POST,
    )


