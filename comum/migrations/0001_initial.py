# Generated by Django 3.2.4 on 2021-08-07 06:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('codigo', models.UUIDField(db_column='cd_endereco', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('latitude', models.CharField(max_length=20, null=True)),
                ('longitude', models.CharField(max_length=20, null=True)),
                ('descricao', models.TextField(null=True)),
                ('cep', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'tb_enderecos',
            },
        ),
        migrations.CreateModel(
            name='OpcaoTag',
            fields=[
                ('codigo', models.UUIDField(db_column='cd_opcaotag', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField(null=True)),
                ('peso', models.PositiveIntegerField(default=1)),
            ],
            options={
                'db_table': 'tb_opcoes_tags',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('codigo', models.UUIDField(db_column='cd_tag', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ativo', models.BooleanField(default=True)),
                ('opcao_tag', models.ForeignKey(db_column='cd_opcao_tag', on_delete=django.db.models.deletion.DO_NOTHING, to='comum.opcaotag')),
                ('tipo', models.ForeignKey(db_column='cd_tipo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.contenttype')),
            ],
            options={
                'db_table': 'tb_tags',
            },
        ),
    ]
