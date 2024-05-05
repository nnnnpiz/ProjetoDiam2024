from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse, reverse_lazy
from .models import Propriedade, Cliente, ESTADOS_CIVIS
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
    anuncios = Propriedade.objects.filter(estado=2)
    if request.method == 'POST':
        distrito = request.POST.get('distrito').lower()  # Access data using the 'name' key
        if distrito:
            anuncios = [anuncio for anuncio in anuncios if anuncio['distrito'] == distrito.lower()]
        cidade = request.Post.get('cidade')
        if cidade:
            anuncios = [anuncio for anuncio in anuncios if anuncio['cidade'] == cidade.lower()]
        freguesia = request.Post.get('freguesia')
        if freguesia:
            anuncios = [anuncio for anuncio in anuncios if anuncio['freguesia'] == freguesia.lower()]
        tipo_propriedade = request.Post.get('tipopropriedade')
        if tipo_propriedade: #TODO VERIFICAR SE ESTA CONDIÇÃO TAMBEM VERIFICA SE A SELEÇÃO DO TIPO DE PROPRIEDADE NAO FOI A DEFAULT
            anuncios = [anuncio for anuncio in anuncios if anuncio['tipo'] == tipo_propriedade]
            subtipo_propriedade = request.Post.get('subtipopropriedade')
            if subtipo_propriedade: #TODO VERIFICAR SE ESTA CONDIÇÃO TAMBEM VERIFICA SE A SELEÇÃO DO SUBTIPO DE PROPRIEDADE NAO FOI A DEFAULT
                anuncios = [anuncio for anuncio in anuncios if anuncio['subtipo'] == subtipo_propriedade]
        classe_energetica = request.Post.get('classeenergetica')
        if classe_energetica: #TODO VERIFICAR SE ESTA CONDIÇÃO TAMBEM VERIFICA SE A SELEÇÃO DA CLASSE ENERGETICA NAO FOI A DEFAULT
            anuncios = [anuncio for anuncio in anuncios if anuncio['classeEnergetica'] == classe_energetica]
        min_wc = request.Post.get('minwc')
        max_wc = request.Post.get('maxwc')
        if min_wc & max_wc:
            anuncios = [anuncio for anuncio in anuncios if anuncio['numWCs'] >= min_wc and anuncio['numWCs'] <=max_wc]
        elif min_wc:
            anuncios = [anuncio for anuncio in anuncios if anuncio['numWCs'] >= min_wc]
        elif max_wc:
            anuncios = [anuncio for anuncio in anuncios if anuncio['numWCs'] <=max_wc]
        min_quartos = request.Post.get('minquartos')
        max_quartos = request.Post.get('maxquartos')
        if min_quartos & max_quartos:
            anuncios = [anuncio for anuncio in anuncios if anuncio['numQuartos'] >= min_quartos and anuncio['numQuartos'] <=max_quartos]
        elif min_quartos:
            anuncios = [anuncio for anuncio in anuncios if anuncio['numQuartos'] >= min_quartos]
        elif max_quartos:
            anuncios = [anuncio for anuncio in anuncios if anuncio['numQuartos'] <=max_quartos]
        min_area = request.Post.get('minarea')
        max_area = request.Post.get('maxarea')
        if min_area & max_area:
            anuncios = [anuncio for anuncio in anuncios if anuncio['area'] >= min_area and anuncio['area'] <=max_area]
        elif min_area:
            anuncios = [anuncio for anuncio in anuncios if anuncio['area'] >= min_area]
        elif max_area:
            anuncios = [anuncio for anuncio in anuncios if anuncio['area'] <=max_area]
        cmobilia = request.Post.get('mobilia')
        smobilia= request.Post.get('smobilia')
        if cmobilia:
            anuncios = [anuncio for anuncio in anuncios if anuncio.get('mobilado', True) is True]
        elif smobilia:
            anuncios = [anuncio for anuncio in anuncios if anuncio.get('mobilado', False) is True]
        canimais = request.Post.get('animais')
        sanimais= request.Post.get('sanimais')
        if canimais:
            anuncios = [anuncio for anuncio in anuncios if anuncio.get('animais', True) is True]
        elif sanimais:
            anuncios = [anuncio for anuncio in anuncios if anuncio.get('animais', False) is True]
        min_preco = request.Post.get('minpreco')
        max_preco = request.Post.get('maxpreco')
        if min_preco & max_preco:
            anuncios = [anuncio for anuncio in anuncios if anuncio['preco'] >= min_preco and anuncio['preco'] <=max_preco]
        elif min_preco:
            anuncios = [anuncio for anuncio in anuncios if anuncio['preco'] >= min_preco]
        elif max_preco:
            anuncios = [anuncio for anuncio in anuncios if anuncio['preco'] <= max_preco]
        negociavel = request.Post.get('negociavel')
        snegociavel= request.Post.get('snegociavel')
        if negociavel:
            anuncios = [anuncio for anuncio in anuncios if anuncio.get('negociavel', True) is True]
        elif snegociavel:
            anuncios = [anuncio for anuncio in anuncios if anuncio.get('negociavel', True) is True]
        criterio_ordenacao = request.Post.get('ordenar')
        if criterio_ordenacao:
            if criterio_ordenacao ==0:
                anuncios.sort(key=lambda x: x['preco'])
            elif criterio_ordenacao ==1:
                anuncios.sort(key=lambda x: x['preco'], reverse=True)
            elif criterio_ordenacao ==2:
                anuncios.sort(key=lambda x: x['area'])
            elif criterio_ordenacao ==3:
                anuncios.sort(key=lambda x: x['area'], reverse=True)
            elif criterio_ordenacao ==4:
                anuncios.sort(key=lambda x: x['dataDeCriacao'])
            elif criterio_ordenacao ==5:
                anuncios.sort(key=lambda x: x['dataDeCriacao'], reverse=True)
    anuncios.sort(key=lambda x: x['highlighted'])
    return render(request, 'romax/resultados.html', context={'anuncios':anuncios})

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
        idade = None if 'idade' in request.POST else int(request.POST['idade']),
        estadoCivil = None if 'idade' in request.POST else request.POST['Estado-Civil'],
        nif = int(request.POST['NIF']),
        cc = request.POST['CC'],
        animais = 'tem-animais' in request.POST,
    )
    return HttpResponseRedirect(reverse('romax:landing_page'))



def informacaopessoal(request):
    return render(request, 'romax/informacao_pessoal.html')