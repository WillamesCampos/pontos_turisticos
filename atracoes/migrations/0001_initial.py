# Generated by Django 3.2.4 on 2021-08-06 23:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('codigo', models.UUIDField(db_column='cd_atracao', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='nm_atracao', max_length=250)),
                ('idade_minima', models.IntegerField()),
                ('descricao', models.TextField()),
                ('horario_abertura', models.DateTimeField()),
                ('horario_fechamento', models.DateTimeField()),
                ('ativo', models.BooleanField(db_column='fl_ativo', default=True)),
                ('funciona_feriados', models.BooleanField(db_column='fl_feriados')),
            ],
            options={
                'db_table': 'tb_atracoes',
            },
        ),
    ]
