from uuid import uuid4
from django.db import models
from atracoes.models import Atracao
from avaliacoes.models import Avaliacao


class Endereco(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_endereco'
    ),
    latitude = models.CharField(
        max_length=20,
        null=True
    )
    longitude = models.CharField(
        max_length=20,
        null=True
    )
    descricao = models.TextField()


class PontoTuristico(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_ponto_turistico'
    )
    nome = models.CharField(
        max_length=300,
        db_column='nm_ponto_turistico'
    )
    descricao = models.TextField()
    atracoes = models.ManyToManyField(
        Atracao,
        related_name='atracao_ponto_turistico',
        related_query_name='atracoes_pontos_turisticos'
    )
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.CASCADE,
        related_name='endereco_ponto_turistico',
        related_query_name='enderecos_pontos_turisticos'
    )
    avaliacoes = models.ManyToManyField(
        Avaliacao,
        related_name='avaliacao_ponto_turistico',
        related_query_name='avaliacoes_pontos_turisticos'
    )
    aprovado = models.BooleanField(
        db_column='fl_aprovado',
        default=False
    )
    foto = models.ImageField(
        upload_to='media/pontos_turisticos'
    )

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        db_table = 'tb_pontos_turisticos'
