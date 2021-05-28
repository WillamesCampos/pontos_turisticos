from django.contrib import admin
from pontos.models import PontoTuristico, Endereco


@admin.action(description='Aprovar pontos turísticos selecionados')
def aprovar_pontos_turisticos(modeladmin, request, queryset):
    return queryset.update(
        aprovado=True
    )


@admin.action(description='Reprovar pontos turísticos selecionados')
def reprovar_pontos_turisticos(modeladmin, request, queryset):
    return queryset.update(
        aprovado=True
    )


@admin.register(PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'nome', 'descricao', 'aprovado'
    ]
    search_fields = [
        'codigo', 'nome', 'aprovado'
    ]
    actions = [
        aprovar_pontos_turisticos,
        reprovar_pontos_turisticos
    ]


@admin.register(Endereco)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'descricao'
    ]
    search_fields = [
        'codigo', 'descricao'
    ]
