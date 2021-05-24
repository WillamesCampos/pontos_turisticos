from uuid import uuid4
from django.db import models


class Atracoes(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
        db_column='cd_atracao'
    )
    nome = models.CharField(
        max_length=250,
        db_column='nm_atracao',
    )
    idade_minima = models.IntegerField()
    descricao = models.TextField()
    horario_abertura = models.DateTimeField()
    horario_fechamento = models.DateTimeField()
    ativo = models.BooleanField(
        default=True,
        db_column='fl_ativo'
    )
    funciona_feriados = models.BooleanField(
        db_column='fl_feriados'
    )

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        db_table = 'tb_atracoes'
