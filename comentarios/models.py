from uuid import uuid4
from django.db import models


class ComentarioMotivo(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
        db_column='cd_comentario-motivo'
    )
    descricao = models.CharField(
        max_length=250,
        db_column='ds_motivo'
    )

    def __str__(self):
        return f'{self.descricao}'

    class Meta:
        db_table = 'tb_comentarios-motivos'


class Comentario(models.Model):
    # usuario = models.ForeignKey(User)
    codigo = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
        db_column='cd_comentario'
    )
    comentario = models.TextField()
    data = models.DateTimeField(
        auto_now=True,
        db_column='dt_data'
    )
    aprovado = models.BooleanField(default=False)
    improprio = models.BooleanField(default=False)
    motivo = models.ForeignKey(
        ComentarioMotivo,
        db_column='cd_comentariomotivo',
        on_delete=models.DO_NOTHING,
        related_name='motivo_comentario'
    )

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        db_table = 'tb_comentarios'
