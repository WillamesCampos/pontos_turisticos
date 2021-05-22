from django.contrib import admin
from atracoes.models import Atracoes


@admin.register(Atracoes)
class AtracoesAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'nome', 'ativo', 'idade_minima'
    ]

    search_fields = [
        'codigo', 'nome', 'ativo'
    ]

