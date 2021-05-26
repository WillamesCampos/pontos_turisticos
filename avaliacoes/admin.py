from django.contrib import admin
from avaliacoes.models import Avaliacao


@admin.action(description='Inativar avaliações selecionadas')
def inativar_avaliacoes(modeladmin, request, queryset):
    return queryset.update(
        ativo=False
    )


@admin.action(description='Ativar avaliações selecionadas')
def ativar_avaliacoes(modeladmin, request, queryset):
    return queryset.update(
        ativo=True
    )


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'comentario', 'nota', 'data', 'ativo'
    ]
    search_fields = [
        'codigo', 'nota', 'ativo'
    ]
    actions = [
        inativar_avaliacoes,
        ativar_avaliacoes
    ]
