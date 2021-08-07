# Generated by Django 3.2.4 on 2021-08-07 06:35

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('comum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('codigo', models.UUIDField(db_column='cd_perfil', default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('acesso', models.IntegerField(choices=[(1, 'COMUM'), (2, 'GUIA TURISTICO'), (3, 'DONO DE ATRACAO'), (4, 'HOSPEDAGEM'), (5, 'RESTAURANTES')], db_column='lv_acesso', default=1)),
                ('documento', models.CharField(max_length=15)),
                ('ativo', models.BooleanField(db_column='fl_ativo', default=True)),
            ],
            options={
                'db_table': 'tb_perfis',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('ativo', models.BooleanField(db_column='fl_ativo', default=True)),
                ('endereco', models.ForeignKey(db_column='cd_endereco', null=True, on_delete=django.db.models.deletion.CASCADE, to='comum.endereco')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('perfil', models.ForeignKey(db_column='cd_perfil', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perfil_usuario', related_query_name='perfis_usuarios', to='usuarios.perfil')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'tb_usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
