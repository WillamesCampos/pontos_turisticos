from django.contrib import admin
from restaurantes.models import Restaurante


@admin.action(description='Desativar restaurantes selecionados')
def desativar_selecionados(modeladmin, request, queryset):
    queryset.update(ativo=False)


@admin.action(description='Ativar restaurantes selecionados')
def ativar_selecionados(modeladmin, request, queryset):
    queryset.update(ativo=True)


@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'nome', 'ponto_turistico', 'ativo'
    ]
    search_fields = [
        'codigo', 'nome', 'ponto_turistico'
    ]
    actions = [
        desativar_selecionados,
        ativar_selecionados
    ]
