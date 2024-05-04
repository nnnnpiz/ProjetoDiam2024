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
    return render(request, 'romax/pesquisa_avancada.html')

def resultados_pesquisa(request):
    anuncios = Anuncio.objects.all()
    if request.method == 'POST':
        distrito = request.POST.get('distrito')  # Access data using the 'name' key
        if distrito:
            #TODO FILTRAR LISTA DE ACORDO COM O DISTRITO PREENCHIDO
        cidade = request.Post.get('cidade')
        if cidade:
            #TODO FILTRAR LISTA DE ACORDO COM O CIDADE PREENCHIDO
        freguesia = request.Post.get('freguesia')
        if freguesia:
            #TODO FILTRAR LISTA DE ACORDO COM A FREGUESIA PREENCHIDA
        tipo_propriedade = request.Post.get('tipopropriedade')
        if tipo_propriedade: #TODO VERIFICAR SE ESTA CONDIÇÃO TAMBEM VERIFICA SE A SELEÇÃO DO TIPO DE PROPRIEDADE NAO FOI A DEFAULT
            #TODO FILTRAR LISTA DE ACORDO COM O TIPOPROPRIEDADE PREENCHIDA
            subtipo_propriedade = request.Post.get('subtipopropriedade')
            if subtipo_propriedade: #TODO VERIFICAR SE ESTA CONDIÇÃO TAMBEM VERIFICA SE A SELEÇÃO DO SUBTIPO DE PROPRIEDADE NAO FOI A DEFAULT
                #TODO FILTRAR LISTA DE ACORDO COM O SUBTIPOPROPRIEDADE PREENCHIDA
        classe_energetica = request.Post.get('classeenergetica')
        if classe_energetica: #TODO VERIFICAR SE ESTA CONDIÇÃO TAMBEM VERIFICA SE A SELEÇÃO DA CLASSE ENERGETICA NAO FOI A DEFAULT
            #TODO FILTRAR LISTA DE ACORDO COM O CLASSENERGETICA PREENCHIDA
        min_wc = request.Post.get('minwc')
        max_wc = request.Post.get('maxwc')
        if min_wc & max_wc:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN E MAX PREENCHIDA - <=min && >=max
        elif min_wc:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN - <=min
        elif max_wc:
        #TODO FILTRAR LISTA DE ACORDO COM O MIN - >= max
        min_quartos = request.Post.get('minquartos')
        max_quartos = request.Post.get('maxquartos')
        if min_quartos & max_quartos:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN E MAX PREENCHIDA - <=min && >=max
        elif min_quartos:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN - <=min
        elif max_quartos:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN - >= max
        min_area = request.Post.get('minarea')
        max_area = request.Post.get('maxarea')
        if min_area & max_area:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN E MAX PREENCHIDA - <=min && >=max
        elif min_area:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN - <=min
        elif max_area:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN - >= max
        cmobilia = request.Post.get('mobilia')
        smobilia= request.Post.get('smobilia')
        if cmobilia:
            #TODO FILTRAR LISTA DE ACORDO COM O VALOR DE CMOBILIA
        elif smobilia:
            #TODO FILTRAR LISTA DE ACORDO COM O VALOR DE SMOBILIA
        canimais = request.Post.get('animais')
        sanimais= request.Post.get('sanimais')
        if canimais:
            #TODO FILTRAR LISTA DE ACORDO COM O VALOR DE CANIMAIS
        elif sanimais:
            #TODO FILTRAR LISTA DE ACORDO COM O VALOR DE SANIMAIS
        min_preco = request.Post.get('minpreco')
        max_preco = request.Post.get('maxpreco')
        if min_preco & max_preco:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN E MAX PREENCHIDA - <=min && >=max
        elif min_preco:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN - <=min
        elif max_preco:
            #TODO FILTRAR LISTA DE ACORDO COM O MIN - >= max
        negociavel = request.Post.get('negociavel')
        snegociavel= request.Post.get('snegociavel')
        if negociavel:
            #TODO FILTRAR LISTA DE ACORDO COM O VALOR DE NEGOCIAVEL
        elif snegociavel:
            #TODO FILTRAR LISTA DE ACORDO COM O VALOR DE SNEGOCIAVEL
        criterio_ordenacao = request.Post.get('ordenar')
        if criterio_ordenacao:
            if criterio_ordenacao ==0:
                #TODO ORDERNAR VIA PRECO ASCENDENTE
            elif criterio_ordenacao ==1:
                #TODO ORDERNAR VIA PRECO DESCENDENTE
            elif criterio_ordenacao ==2:
                #TODO ORDERNAR VIA MAIOR AREA
            elif criterio_ordenacao ==3:
                #TODO ORDERNAR VIA MENOR AREA
            elif criterio_ordenacao ==4:
                #TODO ORDERNAR VIA MAIS RECENTE
            elif criterio_ordenacao ==5:
                #TODO ORDERNAR VIA MAIS ANTIGO
    #ORDERNAR PARA OS ANUNCIOS HIGHLIGHTED SEREM OS PRIMEIROS
    return render(request, 'romax/resultados.html', context={'anuncios':anuncios})

def criar_conta(request):
    pass
