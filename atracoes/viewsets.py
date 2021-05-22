from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin,
    RetrieveModelMixin
)
from rest_framework.response import Response
from atracoes.serializers import AtracaoSerializer
from atracoes.models import Atracoes

class AtracoesViewSet(
    GenericViewSet, ListModelMixin, 
    CreateModelMixin, RetrieveModelMixin
):
    serializer_class = AtracaoSerializer
    def get_queryset(self):
        return Atracoes.objects.filter(
            ativo=True
        )

    @action(
        methods=['GET'],
        detail=False,
        url_path='funciona-feriados',
    )
    def funciona_feriados(self, request):
        queryset = Atracoes.objects.filter(
            ativo=True,
            funciona_feriados=True
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    