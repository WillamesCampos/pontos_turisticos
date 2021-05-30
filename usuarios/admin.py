from django.contrib import admin
from usuarios.models import User, Perfil


@admin.action(description='Desativar selecionados')
def desativar_selecionados(modeladmin, request, queryset):
    return queryset.update(
        ativo=False
    )


@admin.action(description='Desativar selecionados')
def ativar_selecionados(modeladmin, request, queryset):
    return queryset.update(
        ativo=True
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'perfil', 'ativo'
    ]
    search_fields = [
        'name', 'codigo', 'email', 'ativo'
    ]
    actions = [
        desativar_selecionados,
        ativar_selecionados
    ]


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'acesso', 'ativo', 'documento'
    ]
    search_fields = [
        'nome', 'codigo', 'email', 'ativo'
    ]
    actions = [
        desativar_selecionados,
        ativar_selecionados
    ]
