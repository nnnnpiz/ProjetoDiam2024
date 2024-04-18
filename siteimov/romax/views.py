from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def landing_page(request):
    return render(request,'romax/landing_page.html')

def propriedade(request):
    return render(request, 'romax/propriedade.html')

    #TODO fix that
def pesquisa_avancada(request):
    #pagina com form para pesquisa
    pass #TODO

def resultados_pesquisa(request):
    #pesquisa pelo titulo sera based num regex (case insensitive) *titulo*
    pass #TODO


