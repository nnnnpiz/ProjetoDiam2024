from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

MAX_NAME_LEN=400
MAX_MORADA_LEN=400
MAX_TITULO_LEN=300
PASSWORD_LEN = 15
CC_LEN= 10 #TODO see this
NOME_COMPLETO_REGEX_FORMAT = '([A-Z][a-z]{1,} ?)+[A-Z][a-z]{2,}'
TELEMOVEL_REGEX_FORMAT = '9[0-9]{2} ?[0-9]{3} ?[0-9]{3}'
NIF_OR_CC_REGEX_FORMAT='[0-9]{3} ?[0-9]{3} ?[0-9]{3}'

ESTADOS_CIVIS = {
      1: 'Solteiro',
      2: 'Casado',
      3: 'Viúvo',
      4: 'Divorciado',
      5: 'Separado judicialmente de pessoas e bens'
}

CLASSES_ENERGETICAS = {1: 'A+',
                       2: 'A',
                       3: 'B',
                       4: 'B-',
                       5: 'C',
                       6: 'D',
                       7: 'E'
}

CIDADES = {0: 'Grande Lisboa',
           1: 'Grande Porto',
           2: 'Aveiro', 3: 'Braga', 4: 'Coimbra', 5: 'Faro', 6: 'Funchal', 7: 'Guimarães', 8: 'Ponta Delgada', 9: 'Póvoa de Varzim', 10: 'Viana do Castelo', 11: 'Vila Franca de Xira',12:'Viseu'}


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeCompleto = models.CharField(max_length=MAX_NAME_LEN, unique=True)
    telemovel = models.PositiveIntegerField(unique=True)
    idade = models.PositiveSmallIntegerField(blank=True)
    estadoCivil = models.PositiveSmallIntegerField(choices=ESTADOS_CIVIS, blank=True)
    nif = models.PositiveBigIntegerField(default=0)
    cc = models.CharField(max_length=CC_LEN, default=0)
    animais = models.BooleanField(blank=True)
    salvos = models.ManyToManyField('Propriedade')
    urlprofilepic = models.URLField(default='')
class AgenteImobiliario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeCompleto = models.CharField(max_length=MAX_NAME_LEN, unique=True)
    telemovel = models.PositiveIntegerField(default=0)
    idade = models.PositiveSmallIntegerField()
    estadoCivil = models.PositiveSmallIntegerField(choices=ESTADOS_CIVIS)
    nif = models.PositiveBigIntegerField(default=0)
    cc = models.CharField(max_length=CC_LEN,default=0)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeCompleto = models.CharField(max_length=MAX_NAME_LEN, unique=True)
    telemovel = models.PositiveIntegerField(default=0)
    idade = models.PositiveSmallIntegerField()
    estadoCivil = models.PositiveSmallIntegerField(choices=ESTADOS_CIVIS)
    nif = models.PositiveBigIntegerField(default=0)
    cc = models.CharField(max_length=CC_LEN, default=0)


class Propriedade(models.Model):
    animais = models.BooleanField()
    #TODO TipoDePropriedade antonio WTF you wanted here ?
    dataDeCriacao= models.DateTimeField(auto_now_add=True)
    #TODO como raio vamos famos fazer aquilo das cidades, distritos e freguesias
    codigoPostal = models.CharField(max_length=8)
    morada = models.CharField(max_length=MAX_MORADA_LEN)
    numQuartos = models.PositiveSmallIntegerField()
    area = models.FloatField()
    anoConstrucao = models.PositiveSmallIntegerField()
    mobilada = models.BooleanField()
    negociavel = models.BooleanField()
    descricao = models.TextField()
    numWCs = models.PositiveSmallIntegerField()
    classeEnergetica = models.PositiveSmallIntegerField(choices=CLASSES_ENERGETICAS)
    #EstadoAnuncio TODO
    titulo = models.CharField(max_length=MAX_TITULO_LEN)
    highlighted = models.BooleanField()
    preco = models.FloatField()
    cidade = models.PositiveSmallIntegerField(choices=CIDADES)

class PedidosCriacaoAnuncio(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    data_pedido = models.DateField(auto_now_add=True)
    data_fecho = models.DateField(blank=True)

class Oferta(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    propriedade_id = models.ForeignKey('Propriedade', on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    quantia = models.FloatField()
    mensagem = models.TextField(blank=True)

