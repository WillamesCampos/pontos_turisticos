from uuid import uuid4
from django.db import models
from comentarios.models import Comentario
from usuarios.models import User


class Avaliacao(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
        db_column='cd_avaliacao'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        db_column='cd_usuario'
    )
    comentario = models.ForeignKey(
        Comentario,
        null=True,
        on_delete=models.DO_NOTHING,
        db_column='comentario_avaliacao',
        related_name='comentario_avaliacao'
    )
    nota = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        db_table = 'tb_avaliacoes'
