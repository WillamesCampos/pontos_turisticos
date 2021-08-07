from uuid import uuid4
from django.db import models
from django.contrib.contenttypes.models import ContentType


class Endereco(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_endereco'
    )
    latitude = models.CharField(
        max_length=20,
        null=True
    )
    longitude = models.CharField(
        max_length=20,
        null=True
    )
    descricao = models.TextField(
        null=True
    )
    cep = models.CharField(
        max_length=8
    )

    def __str__(self):
        return f'{self.codigo}'

    class Meta:
        db_table = 'tb_enderecos'


class OpcaoTag(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_opcaotag',
    )
    nome = models.CharField(
        max_length=150
    )
    descricao = models.TextField(
        null=True
    )
    peso = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        return f'{self.nome} - peso: {self.peso}'

    class Meta:
        db_table = 'tb_opcoes_tags'


class Tag(models.Model):
    codigo = models.UUIDField(
        default=uuid4,
        editable=False,
        primary_key=True,
        db_column='cd_tag',
    )
    tipo = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
        db_column='cd_tipo',
        null=True
    )
    opcao_tag = models.ForeignKey(
        OpcaoTag,
        on_delete=models.DO_NOTHING,
        db_column='cd_opcao_tag'
    )
    ativo = models.BooleanField(
        default=True
    )

    @property
    def retorna_tipo_tag(self):
        """Retorna o tipo da tag pelo nome do model.

        Returns:
            [str]: [nome do tipo da tag]
            [None]: [se não tiver tipo da tag associada.]
        """
        try:
            return self.tipo.model
        except Exception:
            return None

    def __str__(self):
        return f'{self.codigo} - {self.tipo.model}'

    class Meta:
        db_table = 'tb_tags'
