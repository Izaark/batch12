# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User
from direccion.models import *
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, verbose_name='direccion', null=True, related_name='direccion_usuario')
    telefono = models.ForeignKey(Telefono, verbose_name='telefono', blank=True)
    contribuidor = models.ManyToManyField('self', related_name='amigos_usuario', blank=True)
    def __str__(self):
        if self.first_name:
            return "{0} {1} ".format(self.first_name, self.last_name)
        else:
            return self.username