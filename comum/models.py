from uuid import uuid4
from django.db import models


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
    cep = models.CharField(
        max_length=8
    )
