# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-02 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptante', '0003_persona_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='usuario',
        ),
    ]
