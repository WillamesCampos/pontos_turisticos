# Generated by Django 3.2.3 on 2021-05-30 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comum', '0001_initial'),
        ('pontos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco_ponto_turistico', related_query_name='enderecos_pontos_turisticos', to='comum.endereco'),
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
    ]
