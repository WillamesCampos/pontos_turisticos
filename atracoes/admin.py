from django.contrib import admin
from atracoes.models import Atracoes


@admin.action(description='Inativar as atrações selecionadas')
def inativar_atracoes(modeladmin, request, queryset):
    queryset.update(ativo=False)


@admin.action(description='Ativar as atrações selecionadas')
def ativar_atracoes(modeladmin, request, queryset):
    queryset.update(ativo=True)


@admin.register(Atracoes)
class AtracoesAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'nome', 'ativo', 'idade_minima'
    ]
    search_fields = [
        'codigo', 'nome', 'ativo'
    ]
    actions = [
        inativar_atracoes, ativar_atracoes
    ]
