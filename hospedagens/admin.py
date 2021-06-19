from hospedagens.models import Hospedagem
from django.contrib import admin


@admin.register(Hospedagem)
class HospedagemAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'nome', 'tipo_hospedagem', 'ativo'
    ]
