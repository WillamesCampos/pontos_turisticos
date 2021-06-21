from avaliacoes.models import Avaliacao
from uuid import uuid4
from atracoes.models import Atracao
from comum.models import Endereco
from django.db import models
from pontos.models import PontoTuristico


class Restaurante(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_restaurante'
    )
    ponto_turistico = models.ForeignKey(
        PontoTuristico,
        on_delete=models.DO_NOTHING,
        db_column='cd_ponto_turistico',
        null=True
    )
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.DO_NOTHING,
        db_column='cd_endereco',
    )
    atracao = models.ManyToManyField(
        Atracao,
        through='AtracaoRestaurante',
        db_column='cd_atracao_restaurante',
        related_name='atracao_restaurante',
        related_query_name='atracoes_restaurantes',
    )
    avaliacao = models.ManyToManyField(
        Avaliacao,
        db_column='cd_avaliacao_restaurante',
        related_name='avaliacao_restaurante',
        related_query_name='avaliacoes_restaurantes'
    )
    foto = models.ImageField(
        upload_to='restaurantes/media'
    )

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        db_table = 'tb_restaurantes'


class AtracaoRestaurante(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_restaurante'
    )
    restaurante = models.ForeignKey(
        Restaurante,
        on_delete=models.DO_NOTHING,
        db_column='cd_restaurante',
        related_name='restaurante',
    )
    atracao = models.ForeignKey(
        Atracao,
        db_column='cd_atracao',
        related_name='atracao'
    )

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        db_table = 'tb_atracoes_restaurantes'
