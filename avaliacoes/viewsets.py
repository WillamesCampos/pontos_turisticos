from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin
)

from avaliacoes.serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao


class AvaliacaoViewSet(GenericViewSet, ListModelMixin):

    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        return Avaliacao.objects.filter(
            ativo=True
        )
