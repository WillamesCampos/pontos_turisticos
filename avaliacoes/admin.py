from django.contrib import admin
from avaliacoes.models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'comentario', 'nota', 'data', 'ativo'
    ]
    search_fields = [
        'codigo', 'nota', 'ativo'
    ]
