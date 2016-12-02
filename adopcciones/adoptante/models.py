from __future__ import unicode_literals
from django.db import models
from usuario.models import Usuario
from direccion.models import Direccion

class Persona(models.Model):
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    name = models.CharField(max_length=15,blank=False,null=False)
    last_name = models.CharField(max_length=20,blank=False,null=False)
    age = models.IntegerField(default=0)
    telephone = models.IntegerField(default=0,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    home = models.TextField(blank=False,null=True)
    #Relations
    usuario = models.ForeignKey(Usuario,null=False,blank=False,related_name='usuario_persona')
    direccion = models.ForeignKey(Direccion,null=False,blank=True,related_name='persona_direccion')
    def __str__(self):
        return "Es adoptado por {0}".format(self.name)

class Solicitud(models.Model):
    person = models.ForeignKey(Persona, null=True, blank=True, related_name='persona_solicitud')
    razones = models.TextField()
    def __str__(self):
    	return self.razones