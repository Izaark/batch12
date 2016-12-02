from __future__ import unicode_literals
from django.db import models
from adoptante.models import Persona

class Educacion(models.Model):
	name = models.CharField(max_length=25,blank=False, null=False)
	def __str__(self):
		return self.name

class Infante(models.Model):

    class Meta:
        verbose_name = "Infante"
        verbose_name_plural = "Infantes"
        #Attrubutes
    name = models.CharField(max_length=15,blank=False,null=False)
    sex = models.CharField(max_length=20,blank=False,null=False)
    age = models.IntegerField(default=0)
    date = models.DateField()

    #Reltions
    persona = models.ForeignKey(Persona, null=False,blank=False, on_delete=models.CASCADE, related_name='persona_infante')
    educacion = models.ManyToManyField(Educacion, related_name='educacion_infante')


    def __str__(self):
        return "Hola {0}".format(self.name)