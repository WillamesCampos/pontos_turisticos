from django.contrib import admin
from comentarios.models import Comentario


@admin.action(description='Tornar impróprios comentários selecionados.')
def tornar_improprio(queryset):
    queryset.update(
        improprio=True
    )


@admin.action(description='Reprovar comentários selecionados.')
def reprovar_comentarios(queryset):
    queryset.update(
        aprovado=False
    )


@admin.action(description='Aprovar comentários selecionados.')
def aprovar_comentarios(queryset):
    queryset.update(
        aprovado=True
    )


@admin.register(Comentario)
class AdminComentario(admin.ModelAdmin):
    list_display = [
        'codigo', 'comentario', 'motivo', 'data', 'improprio', 'aprovado'
    ]
    search_fields = ['codigo', 'aprovado', 'improprio']
    action = [
        tornar_improprio,
        reprovar_comentarios,
        aprovar_comentarios
    ]
