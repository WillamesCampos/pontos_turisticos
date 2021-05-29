from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models


class Perfil(models.Model):

    ACESSO_CHOICES = [
        (1, 'COMUM'),
        (2, 'GUIA TURISTICO'),
        (3, 'DONO DE ATRACAO')
    ]

    codigo = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
        db_column='cd_perfil'
    )
    acesso = models.IntegerField(
        choices=ACESSO_CHOICES,
        db_column='lv_acesso',
        default=1
    )
    documento = models.CharField(
        max_length=15
    )
    ativo = models.BooleanField(
        db_column='fl_ativo',
        default=True
    )

    def __str__(self):
        return f'{self.acesso} - {self.codigo}'

    class Meta:
        db_table = 'tb_perfis'


class User(AbstractUser):
    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        db_column='cd_perfil',
        related_name='perfil_usuario',
        related_query_name='perfis_usuarios',
        null=True
    )
    ativo = models.BooleanField(
        default=True,
        db_column='fl_ativo'
    )

    def __str__(self):
        return f'{self.email}'

    class Meta:
        db_table = 'tb_usuarios'
