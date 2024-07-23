from django import template
from cadastro.models import banner_personagem  # Substitua 'your_app' pelo nome real do seu app

register = template.Library()

@register.filter
def caminho_display(value):
    # Cria um dicionário a partir das escolhas
    choices_dict = dict(banner_personagem.caminho_choices)
    return choices_dict.get(value, '')