# Generated by Django 3.2.4 on 2021-08-07 06:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('comum', '0001_initial'),
        ('pontos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospedagem',
            fields=[
                ('codigo', models.UUIDField(db_column='cd_hospedagem', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='nm_hospedagem', max_length=250)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(upload_to='hospedagens/media')),
                ('nota_de_preco', models.IntegerField(choices=[(1, 'MUITO ACESSÍVEL'), (2, 'ACESSÍVEL'), (3, 'PADRÃO'), (4, 'PREMIUM'), (5, '5 ESTRELAS')], db_column='nt_faixa_preco')),
                ('voltagem', models.CharField(choices=[('110', '110V'), ('220', '220V'), ('ambos', 'AMBOS')], db_column='fx_voltagem', max_length=6)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, db_column='dt_criacao')),
                ('ativo', models.BooleanField(db_column='fl_ativo', default=True)),
                ('avaliacoes', models.ManyToManyField(db_column='cd_avaliacao_hospedagem', related_name='avaliacao_hospedagem', related_query_name='avaliacoes_hospedagens', to='avaliacoes.Avaliacao')),
                ('endereco', models.ForeignKey(db_column='cd_endereco_hospedagem', on_delete=django.db.models.deletion.CASCADE, to='comum.endereco')),
            ],
            options={
                'db_table': 'tb_hospedagens',
            },
        ),
        migrations.CreateModel(
            name='TipoHospedagem',
            fields=[
                ('codigo', models.UUIDField(db_column='cd_tipohospedagem', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='nm_tipohospedagem', max_length=250)),
                ('descricao', models.TextField()),
            ],
            options={
                'db_table': 'tb_tipos_hospedagens',
            },
        ),
        migrations.CreateModel(
            name='PontoHospedagem',
            fields=[
                ('codigo', models.UUIDField(db_column='cd_pontohospedagem', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hospedagem', models.ForeignKey(db_column='cd_hospedagem_pontohospedagem', on_delete=django.db.models.deletion.DO_NOTHING, to='hospedagens.hospedagem')),
                ('ponto_turistico', models.ForeignKey(db_column='cd_pontoturistico_pontohospedagem', on_delete=django.db.models.deletion.DO_NOTHING, to='pontos.pontoturistico')),
            ],
            options={
                'db_table': 'tb_pontos_hospedagens',
            },
        ),
        migrations.AddField(
            model_name='hospedagem',
            name='ponto_turistico',
            field=models.ManyToManyField(related_name='cd_pontoturistico_hospedagem', related_query_name='cd_pontosturisticos_hospedagens', through='hospedagens.PontoHospedagem', to='pontos.PontoTuristico'),
        ),
        migrations.AddField(
            model_name='hospedagem',
            name='tipo_hospedagem',
            field=models.ForeignKey(db_column='cd_tipo_hospedagem', on_delete=django.db.models.deletion.DO_NOTHING, to='hospedagens.tipohospedagem'),
        ),
    ]
