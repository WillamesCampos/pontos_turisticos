# Generated by Django 3.2.3 on 2021-05-29 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='usuario',
            field=models.ForeignKey(db_column='cd_usuario', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
