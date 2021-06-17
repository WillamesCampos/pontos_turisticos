from uuid import uuid4
from django.db import models

from avaliacoes.models import Avaliacao
from comum.models import Endereco
from pontos.models import PontoTuristico


class TipoHospedagem(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_tipohospedagem'
    )
    nome = models.CharField(
        max_length=250,
        db_column='nm_tipohospedagem'
    )


class Hospedagem(models.Model):
    FAIXAS_DE_PRECO = [
        (1, 'MUITO ACESSÍVEL'),
        (2, 'ACESSÍVEL'),
        (3, 'PADRÃO'),
        (4, 'PREMIUM'),
        (5, '5 ESTRELAS')
    ]

    VOLTAGEM = [
        ('110', '110V')
        ('220', '220V')
        ('ambos', 'AMBOS')
    ]

    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_hospedagem'
    )
    nome = models.CharField(
        max_length=250,
        db_column='nm_hospedagem'
    )
    tipo_hospedagem = models.ForeignKey(
        TipoHospedagem,
        on_delete=models.DO_NOTHING,
        db_column='cd_tipo_hospedagem'
    )
    descricao = models.TextField()
    ponto_turistico = models.ManyToManyField(
        through='PontoHospedagem',
        related_name='cd_pontoturistico_hospedagem',
        related_query_name='cd_pontosturisticos_hospedagens'
    )
    avaliacoes = models.ForeignKey(
        Avaliacao,
        on_delete=models.CASCADE,
        db_column='cd_avaliacao_hospedagem'
    )
    endereco = models.ForeignKey(
        Endereco,
        on_delete=models.CASCADE,
        db_column='cd_endereco_hospedagem'
    )
    nota_de_preco = models.IntegerField(
        choices=FAIXAS_DE_PRECO,
        db_column='nt_faixa_preco'
    )
    voltagem = models.CharField(
        choices=VOLTAGEM,
        max_length=6
    )


class PontoHospedagem(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_pontohospedagem'
    )
    ponto_turistico = models.ForeignKey(
        PontoTuristico,
        on_delete=models.DO_NOTHING,
        db_column='cd_pontoturistico_pontohospedagem'
    )
    hospedagem = models.ForeignKey(
        Hospedagem,
        on_delete=models.DO_NOTHING,
        db_column='cd_hospedagem_pontohospedagem'
    )
