# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-30 18:10
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_postal', models.CharField(default='', max_length=11)),
                ('nombre', models.CharField(default='', max_length=300, verbose_name='Colonia')),
                ('municipio', models.CharField(default='', max_length=60, verbose_name='Delegacion o municipio')),
                ('ciudad', models.CharField(default='', max_length=128, verbose_name='Ciudad')),
                ('estado', models.CharField(default='DF', max_length=60, verbose_name='Estado')),
                ('pais', models.CharField(default='Mexico', max_length=300, verbose_name='Pais')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_telefono', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('colonia_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='direccion.Colonia')),
                ('slug', models.SlugField(max_length=300)),
                ('calle_y_numero', models.CharField(default='', editable=False, max_length=300, verbose_name='Calle y numero')),
                ('calle', models.CharField(default='', max_length=220, verbose_name='Calle')),
                ('numero_exterior', models.CharField(default='', max_length=40, verbose_name='Numero exterior')),
                ('numero_interior', models.CharField(blank=True, default='', max_length=40, verbose_name='Numero interior')),
                ('longitud', models.DecimalField(blank=True, decimal_places=14, default=0, max_digits=17, verbose_name='Coordenadas UTM-E')),
                ('latitud', models.DecimalField(blank=True, decimal_places=14, default=0, max_digits=17, verbose_name='Coordenadas UTM-N')),
                ('enlace_mapa', models.URLField(blank=True, default='')),
                ('creado_el', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('modificado_el', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Direcciones',
            },
            bases=('direccion.colonia',),
        ),
    ]
