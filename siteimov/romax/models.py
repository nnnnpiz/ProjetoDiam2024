from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

MAX_NAME_LEN=400
MAX_MORADA_LEN=400
MAX_TITULO_LEN=300
ESTADOS_CIVIS =  {
      1 : 'Solteiro',
      2 : 'Casado',
      3 : 'Viúvo',
      4 : 'Divorciado',
      5 : 'Separado judicialmente de pessoas e bens'
}
CLASSES_ENERGETICAS = {1: 'A+', 2: 'A', 3: 'B', 4: 'B-', 5: 'C', 6: 'D', 7: 'E'}
class BasicUser(User):
    NomeCompleto = CharField(max=MAX_NAME_LEN, unique=true)
    Email= EmailField(unique=true) # Acho que ja existe na super class

    # TODO Telemovel =  vai ter o +351 ? se nao é PositiveIntegerField()
    Idade = models.PositiveSmallIntegerField()
    EstadoCivil = models.PositiveSmallIntegerField(choices=ESTADOS_CIVIS)
    #NIF, CC

class Propriedade(models.Model):
    Id = BigAutoField()
    Animals = BooleanField()
    #TODO TipoDePropriedade antonio WTF you wanted here ?
    DataDeCriacao= models.DateTimeField(auto_now_add=true)
    #TODO como raio vamos famos fazer aquilo das cidades, distritos e freguesias
    CodigoPostal = models.CharField(max=8)
    Morada = models.CharField(max=MAX_MORADA_LEN)
    NumQuartos = models.PositiveSmallIntegerField()
    Area = models.FloatField()
    AnoConstrucao = models.PositiveSmallIntegerField()
    Mobilada = BooleanField()
    Negociavel = BooleanField()
    Descricao = TextField()
    NumWCs = models.PositiveSmallIntegerField()
    ClasseEnergetica = models.PositiveSmallIntegerField(choices=CLASSES_ENERGETICAS)
    #EstadoAnuncio TODO
    Titulo = models.CharField(max=MAX_TITULO_LEN)
    Highlighted = BooleanField()