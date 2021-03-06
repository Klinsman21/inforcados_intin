# Generated by Django 2.0.3 on 2018-08-29 22:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Letras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letra', models.CharField(max_length=150, verbose_name='letra')),
                ('partidaId', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='id-partida')),
                ('visible', models.BooleanField(default=False, verbose_name='visivel')),
            ],
            options={
                'verbose_name': 'letra',
                'verbose_name_plural': 'letras',
            },
        ),
        migrations.CreateModel(
            name='Palavra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palavra', models.CharField(max_length=150, verbose_name='palavra')),
                ('dica', models.CharField(max_length=150, verbose_name='dica')),
            ],
            options={
                'verbose_name': 'palavra',
                'verbose_name_plural': 'palavras',
            },
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='id-user')),
                ('allTrue', models.BooleanField(default=False, verbose_name='final')),
                ('image', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='image')),
                ('state', models.BooleanField(default=True, verbose_name='estado')),
                ('dica', models.CharField(max_length=150, verbose_name='dica')),
            ],
            options={
                'verbose_name': 'partida',
                'verbose_name_plural': 'partidas',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=150, verbose_name='userName')),
                ('userId', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='id-user')),
                ('Individualpontos', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='pointsI')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
