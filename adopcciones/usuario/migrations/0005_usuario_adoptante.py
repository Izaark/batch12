# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adoptante', '0004_remove_persona_usuario'),
        ('usuario', '0004_usuario_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='adoptante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='adoptante_usuario', to='adoptante.Persona'),
            preserve_default=False,
        ),
    ]