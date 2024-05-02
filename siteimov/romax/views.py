from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def landing_page(request):
    return render(request, 'romax/landing_page.html',
                      context={'highlighted_properties': [i for i in range(10)]})

def login(request):
    print( request.POST['user-email'], request.POST['password'] )
    #request.POST['user-email']
    #request.POST['password']
def propriedade(request, id):
    return render(request, 'romax/propriedade.html', context={
    })
    try:
        Propriedade.objects.get(id=id)
        return render(request, 'romax/propriedade.html', context={
        })
    except ObjectDoesNotExist:
        #Filipe cria aqui a pagina do propriedade n existe
        return render(request, 'romax/propriedade.html', context={
        })


    #TODO fix that
def pesquisa_avancada(request):
    #pagina com form para pesquisa
    pass #TODO

def resultados_pesquisa(request):
    #pesquisa pelo titulo sera based num regex (case insensitive) *titulo*
    pass #TODO

def criar_conta(request):
    pass
