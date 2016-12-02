from rest_framework import serializers
from .models import Infante,Educacion

class EducacionSerializer(serializers.ModelSerializer):
	class Meta:
		model= Educacion
		fields=['name']

class InfanteSerializer(serializers.ModelSerializer):
	educacion_infante = EducacionSerializer(source="educacion", many=True, read_only=True)
	class Meta:
		model = Infante
		fields = ['name','sex','age','educacion_infante']