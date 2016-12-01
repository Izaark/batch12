from rest_framework import serializers
from .models import Usuario

class AmigosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = ['first_name','last_name']

class UsuarioSerializer(serializers.ModelSerializer):
	amigos_usuario = AmigosSerializer(source="contribuidor", many=True, read_only=True)
	class Meta:
		model = Usuario
		fields = ['id','username','first_name','last_name','email','is_active','direccion','telefono','amigos_usuario']
	