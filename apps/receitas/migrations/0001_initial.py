# Generated by Django 3.2.6 on 2021-09-03 12:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=200)),
                ('ingredientes', models.TextField()),
                ('modo_preparo', models.TextField()),
                ('tempo_preparo', models.IntegerField()),
                ('rendimento', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('data_receita', models.DateField(blank=True, verbose_name=datetime.datetime(2021, 9, 3, 9, 11, 54, 390592))),
                ('teste_field', models.CharField(max_length=10)),
            ],
        ),
    ]