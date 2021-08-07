from django.contrib import admin

from comum.models import Tag, OpcaoTag


@admin.action(description='desativar tags selecionadas')
def desativar_tags(modeladmin, request, queryset):
    return queryset.update(
        ativo=False
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'tipo', 'opcao_tag',
        'ativo'
    ]

    search_fields = [
        'codigo', 'tipo__nome'
    ]

    actions = [
        desativar_tags,
    ]


@admin.register(OpcaoTag)
class OpcaoTagAdmin(admin.ModelAdmin):
    list_display = [
        'codigo', 'nome', 'peso'
    ]

    search_fields = [
        'codigo', 'nome', 'peso'
    ]
