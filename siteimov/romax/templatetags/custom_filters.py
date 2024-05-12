from django import template

from romax.models import CIDADES, CLASSES_ENERGETICAS,TIPOS_PROPRIEDADES,SUBTIPO_PROPRIEDADES

register = template.Library()


@register.filter(name='cidade_name')
def cidade_name(value):
    return CIDADES.get(value, '')

@register.filter(name='classe_name')
def classe_name(value):
    return CLASSES_ENERGETICAS.get(value, '')

@register.filter(name='tipo_name')
def tipo_name(value):
    return TIPOS_PROPRIEDADES.get(value, '')

@register.filter(name='subtipo_name')
def subtipo_name(value):
    return SUBTIPO_PROPRIEDADES.get(value, '')