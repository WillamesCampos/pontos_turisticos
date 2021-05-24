from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, UpdateModelMixin, ListModelMixin
)
from comentarios.models import Comentario
from comentarios.serializers import ComentarioSerializer


class ComentarioViewSet(
    GenericViewSet, CreateModelMixin, UpdateModelMixin,
    ListModelMixin
):

    serializer_class = ComentarioSerializer

    def get_queryset(self):
        return Comentario.objects.filter(
            aprovado=True
        )
