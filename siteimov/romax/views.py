import re
import string

from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.views import APIView

#from utils import handle_uploaded_file
from .models import CIDADES, CLASSES_ENERGETICAS, SYMBOLS_PASS, SUBTIPO_PROPRIEDADES,TIPOS_PROPRIEDADES
from .models import Propriedade, Cliente, PASSWORD_LEN, ESTADOS_CIVIS, MAX_NAME_LEN, NOME_COMPLETO_REGEX_FORMAT, \
    TELEMOVEL_REGEX_FORMAT, NIF_OR_CC_REGEX_FORMAT, AgenteImobiliario, PedidosCriacaoAnuncio
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .serializers import LoginSerializer

EMAIL_VALIDATION_REGEX='^[a-z._-]+@[a-z]+.[a-z]+$' #TODO Voltar aqui


EMAIL_VALIDATION_REGEX_COMPILE = re.compile(EMAIL_VALIDATION_REGEX)
NOME_COMPLETO_REGEX_FORMAT_COMPILE = re.compile(NOME_COMPLETO_REGEX_FORMAT)
TELEMOVEL_REGEX_FORMAT_COMPILE = re.compile(TELEMOVEL_REGEX_FORMAT)
NIF_OR_CC_REGEX_FORMAT_COMPILE = re.compile(NIF_OR_CC_REGEX_FORMAT)
# Create your views here.

def landing_page(request):
    context = {
        'highlighted_properties': Propriedade.objects.filter(highlighted=True), #TODO ver depois criterio para highlighted ! (ex: mais favoritos, mendy quer por agora todas as highlighted)
        'CIDADES': CIDADES
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
                      context={'propriedade': propriedade,
                               'favorito': Cliente.objects.get(user=request.user).salvos.filter(pk=propriedade.id).exists()
                               }
                      )
    except (KeyError, Propriedade.DoesNotExist):
        return render(request, 'romax/propriedade_notfound.html', context={
        })

def pesquisa_avancada(request):
    ordernar = [ "Preço ascendente", "Preço descendente", "Maior área", "Menor área", "Mais recente", "Mais antigo"]

    return render(request, 'romax/pesquisa_avancada.html', context={
       'ordernar' : zip(range(1,len(ordernar) ),ordernar),
        'CIDADES':CIDADES,
        'TIPOS_PROPRIEDADES':TIPOS_PROPRIEDADES,
        'SUBTIPO_PROPRIEDADES': SUBTIPO_PROPRIEDADES,
        'CLASSES_ENERGETICAS': CLASSES_ENERGETICAS
    })

def resultados_pesquisa(request):
    #TODO possivel incremento pesquisa pelo titulo sera based num regex (case insensitive) *titulo*

    parametros_pesquisa = request.POST

    parametros_pesquisa['Cidade']
    parametros_pesquisa['titulo']

    pesquisa_cliente = Q()

    id_cidade=int(parametros_pesquisa['Cidade'])
    match id_cidade:
        case -1:
            pass
        case id_cidade if id_cidade in range(len(CIDADES)):
            pesquisa_cliente.add(Q(cidade=id_cidade),Q.AND)
        case _:
            pass #TODO lancçar erro ou algo

    titulo = parametros_pesquisa.get('titulo', '')

    if titulo != '':
        pesquisa_cliente &= Q(titulo__icontains=titulo)
        #pesquisa_cliente.add(Q(titulo=parametros_pesquisa['titulo']), Q.AND)

    return render(request, 'romax/resultados_pesquisas.html', context ={
        'Resultados': Propriedade.objects.filter(pesquisa_cliente)
    })

def criar_conta_page(request):
    return render(request, 'romax/criar_conta_page.html', context = {
        'ESTADOS_CIVIS' : ESTADOS_CIVIS,
        'MAX_NAME_LEN' : MAX_NAME_LEN,
        'NOME_COMPLETO_REGEX_FORMAT': NOME_COMPLETO_REGEX_FORMAT,
        'TELEMOVEL_REGEX_FORMAT' : TELEMOVEL_REGEX_FORMAT,
        'NIF_OR_CC_REGEX_FORMAT' : NIF_OR_CC_REGEX_FORMAT,
        'PASSWORD_LEN' : PASSWORD_LEN,
        'SYMBOLS_PASS' : SYMBOLS_PASS,
        'PASSWORD_LEN' : PASSWORD_LEN
    })

def criar_conta(request):
    # TODO page para se nao foi possivel criar conta (failed server-side validation or server error (5xx))

    #Validar o email
    email_valido = type(re.fullmatch(EMAIL_VALIDATION_REGEX_COMPILE,request.POST['email'])) == type(re.Match)

    #validar o nome completo
    nome_completo = request.POST['nome-completo']
    is_valid_length = len(nome_completo) <= MAX_NAME_LEN
    is_valid_format = type(re.fullmatch(NOME_COMPLETO_REGEX_FORMAT_COMPILE, nome_completo)) == type(re.Match)


    #validar Telemovel
    telemovel = request.POST['telemovel']
    tel_valido = type(re.fullmatch(TELEMOVEL_REGEX_FORMAT_COMPILE, telemovel) )== type(re.Match)
    telemovel = transformar_em_tel(telemovel)

    #Validar idade se Cliente inseriu uma
    if('idade' in request.POST):
        idade = int(request.POST['idade'])

        idade_valida = 18 <= idade <=122
        del idade

    #validar Estado Civil e Cliente inseriu um
    estado_civil_valido = request.POST['Estado-Civil'] in list(ESTADOS_CIVIS.keys()) + ['']

    #validar password
    pass_valida = pass_tem_requisitos(request.POST['password'])

    if( not (email_valido and pass_valida and estado_civil_valido and  idade_valida and tel_valido and is_valid_format and is_valid_length) ):
        return HttpResponse(status=401, content="Es retardado")
    #url:
    myfile = request.FILES.get('myfile')
    if myfile:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        # verificar se foto ja existe no media dir
        if fs.exists(myfile.name):
            fs.delete(myfile.name)

        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
    else:
        uploaded_file_url=''



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
            urlprofilepic = uploaded_file_url
        )
    except:
        user.delete()
    return HttpResponseRedirect(reverse('romax:landing_page'))



def informacaopessoal(request):
    return render(request, 'romax/informacao_pessoal.html')

def salvar_alteracoes_conta(request):
    if request.method == 'POST':
        re.fullmatch(EMAIL_VALIDATION_REGEX_COMPILE, request.POST['email'])

        # validar o nome completo
        nome_completo = request.POST['nome-completo']
        len(nome_completo) <= MAX_NAME_LEN
        re.fullmatch(NOME_COMPLETO_REGEX_FORMAT_COMPILE, nome_completo)

        # validar Telemovel
        telemovel = request.POST['telemovel']
        re.fullmatch(TELEMOVEL_REGEX_FORMAT_COMPILE, telemovel)
        telemovel = telemovel.replace(' ', '')

        # Validar idade se Cliente inseriu uma
        if ('idade' in request.POST):
            idade = int(request.POST['idade'])

            18 <= idade <= 122
            del idade

        # validar Estado Civil e Cliente inseriu um

        # validar password
        pass_valida = pass_tem_requisitos()

        #buscar user: (se quiser aceder ao cliente p mudar fzr objc.cliente
        objc = User.objects.get(username=request.user.username)

        # url:
        if 'myfile' in request.FILES:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            # verificar se foto ja existe no media dir
            if fs.exists(myfile.name):
                fs.delete(myfile.name)

            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
        else:
            uploaded_file_url = objc.cliente.urlprofilepic

        objc.username = request.POST['email']
        objc.email = request.POST['email']
        objc.save()
        objc.cliente.nomeCompleto = nome_completo
        objc.cliente.idade = int(request.POST['idade'])
        objc.cliente.estadoCivil = int(request.POST['Estado-Civil'])
        objc.cliente.animais = 'tem-animais' in request.POST
        objc.cliente.telemovel = int(telemovel)
        objc.cliente.nif = int(request.POST['NIF'])
        objc.cliente.cc = request.POST['CC']
        objc.cliente.urlprofilepic = uploaded_file_url
        objc.cliente.save()

        return HttpResponseRedirect(reverse('romax:informacaopessoal'))
    else:
        return render(request, 'romax/informacao_pessoal.html')

def sobre_page(request):
    return render(request, 'romax/sobre_page.html')

#TODO @login_required()
def criar_propriedade_pagina(request, pedido_id):
    try:
        agente = AgenteImobiliario.objects.get(user=request.user)
        pedido = PedidosCriacaoAnuncio.objects.get(id=pedido_id)
        user = User.objects.get(id=pedido.user_id)
        pedinte = Cliente.objects.get(user=user)
    except models.Model.DoesNotExist:
        return HttpResponse(status=401, content="Não tens autorização para aceder")
    if request.method == 'POST':

        # TODO validacao

        propriedade_criada = Propriedade.objects.create(
            animais=request.POST['animais'],
            # TODO TipoDePropriedadeantonio WTF you wanted here ?
            codigoPostal=request.POST['codigo-postal-1'] + '-' + request.POST['codigo-postal-2'],
            morada=request.POST['morada'],
            numQuartos=request.POST['n-quartos'],
            area=request.POST['area'],
            anoConstrucao=request.POST['ano-construcao'],
            mobilada='Mobilada' in request.POST,
            negociavel='Negociavel' in request.POST,
            descricao=request.POST['descricao'],
            numWCs=request.POST['n-casas-banho'],
            classeEnergetica=request.POST['class-energetica'],
            # EstadoAnuncio TODO
            titulo=request.POST['titulo'],
            highlighted=request.POST[''],
            preco=request.POST['preco'],
            cidade=request.POST['Cidade']
        )
        #pedido.data_fecho = TODO
        pedido.tratado_por = agente
        pedido.save()

        pedinte.add(propriedade_criada)
        if 'foto_principal' in request.FILES:
            handle_uploaded_file('diretory: str', f'{propriedade_criada.id}_P', request.FILES['foto_principal'])
            # 'propriedade_criada_P'

        restantes_fotos = request.FILES.get('restantes_fotos', [])
        for i, img in enumerate(restantes_fotos):
            handle_uploaded_file('diretory: str', f'{propriedade_criada.id}_{i}', restantes_fotos)
    else:
        return render(request, 'romax/criar_propriedade_page.html', context={
            'CIDADES' : CIDADES,
            'CLASSES_ENERGETICAS':  CLASSES_ENERGETICAS,
            #'Dono' : pedinte.nomeCompleto
        })

#################   Utilies   #################

def transformar_em_tel(tel_str : str) -> int :
    return int(re.sub('\s+', '', tel_str))
def handle_uploaded_file(diretory: str, filename: str, file):
    with open(f'{diretory}/{filename}', "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def pass_tem_requisitos(password: str)-> bool:
    def tem_maiscula(password: str)-> bool:
        for chr in password:#ver se tem uma maiscula
            if(chr in string.ascii_uppercase):
                return True
        return False
    def tem_minuscula(password: str)-> bool:
        for chr in password:#ver se tem uma minuscula
            if(chr in string.ascii_lowercase):
                return True
        return False
    def tem_numero(password: str)-> bool:
        for chr in password:#ver se tem uma minuscula
            if(chr in "1234567890"):
                return True
        return False
    def tem_simbolo(password: str)-> bool:
        for chr in password:#ver se tem uma minuscula
            if(chr in SYMBOLS_PASS):
                return True
        return False

    return tem_simbolo(password) and tem_minuscula(password) and tem_numero(password) and tem_maiscula(password) and len(password) >=PASSWORD_LEN


def favorito(request, propriedade_id):

    usr = Cliente.objects.get(user=request.user)
    prop = Propriedade.objects.get(pk=propriedade_id)

    if not usr.salvos.filter(pk=prop.pk).exists():
        usr.salvos.add(prop)
        print("prop added")
    else:
        usr.salvos.remove(prop)

    return render(request, 'romax/propriedade.html',
                  context={'propriedade': prop})
#retornar HTPP RESPONSE


def favoritos_page(request):
    usr=Cliente.objects.get(user=request.user)
    props_fav=usr.salvos.all()
    return render(request, 'romax/resultados_pesquisas.html', context={
        'Resultados': props_fav
    })

def propriedades_all(request):
    return render(request, 'romax/resultados_pesquisas.html', context={
        'Resultados': Propriedade.objects.all()
    })

def imoveis_luxo(request):
    return render(request, 'romax/resultados_pesquisas.html', context={
        'Resultados': Propriedade.objects.filter(preco__gt=150000)
    })

def search_avancada_treat(request):
    if request.method == 'POST':

        cidade = request.POST.get('cidades')
        if cidade:
            cidade = int(cidade)
        else:
            cidade = None

        tipopropriedade = request.POST.get('tipopropriedade')
        if tipopropriedade:
            tipopropriedade = int(tipopropriedade)
        else:
            tipopropriedade = None


        subtipopropriedade = request.POST.get('subtipopropriedade')
        if subtipopropriedade:
            subtipopropriedade = int(subtipopropriedade)
        else:
            subtipopropriedade = None


        classeenergetica = request.POST.get('classeenergetica')
        if classeenergetica:
            classeenergetica = int(classeenergetica)
        else:
            classeenergetica = None

        minwc = request.POST.get('minwc', 0)
        if minwc:
            minwc = int(minwc)
        else:
            minwc = None


        maxwc = request.POST.get('maxwc', 0)
        if maxwc:
            maxwc = int(maxwc)
        else:
            maxwc = None


        minquartos = request.POST.get('minquartos',0)
        if minquartos:
            minquartos = int(minquartos)
        else:
            minquartos = None

        maxquartos = request.POST.get('maxquartos',0)
        if maxquartos:
            maxquartos = int(maxquartos)
        else:
            maxquartos = None

        minarea = request.POST.get('minarea',0)
        if minarea:
            minarea = float(minarea)
        else:
            minarea = None

        maxarea = request.POST.get('maxarea',0)
        if maxarea:
            maxarea = float(maxarea)
        else:
            maxarea = None


        mobilia = request.POST.get('mobilia')
        animais = request.POST.get('animais')
        minpreco = request.POST.get('minpreco')
        maxpreco = request.POST.get('maxpreco')
        negociavel = request.POST.get('negociavel')
        ordenar = request.POST.get('ordenar')

        # Construct filter parameters
        filters = {}

        if cidade:
            filters['cidade'] = cidade
        if tipopropriedade:
            filters['tipo'] = tipopropriedade
        if subtipopropriedade:
            filters['subtipo'] = subtipopropriedade
        if classeenergetica:
            filters['classeEnergetica'] = classeenergetica
        if minwc:
            filters['numWCs__gte'] = minwc
        if maxwc:
            filters['numWCs__lte'] = maxwc

        if minquartos:
            filters['numQuartos__gte'] = minquartos
        if maxquartos:
            filters['numQuartos__lte'] = maxquartos

        if minarea:
            filters['area__gte'] = minarea
        if maxarea:
            filters['area__lte'] = maxarea




        if mobilia:
            filters['mobilado'] = True if mobilia == 'true' else False
        if animais:
            filters['animais_estimacao'] = True if animais == 'true' else False
        if minpreco:
            filters['preco__gte'] = minpreco
        if maxpreco:
            filters['preco__lte'] = maxpreco
        if negociavel:
            filters['preco_negociavel'] = True if negociavel == 'true' else False

        if filters:
            propriedades = Propriedade.objects.filter(**filters)
        else:
            propriedades = Propriedade.objects.none()

        return render(request, 'romax/resultados_pesquisas.html', context={
            'Resultados': propriedades
        })

    return HttpResponse('Method Not Allowed', status=405)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key}, safe=False)
        else:
            return JsonResponse("{'error': 'Credenciais inválidas'}", safe=False, status=400)











