from atracoes.serializers import AtracaoSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin,
    RetrieveModelMixin
)
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
    