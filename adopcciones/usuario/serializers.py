from rest_framework import serializers
from .models import Usuario
#from adoptante.serializers import SolicitudSerializer
class AmigosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Usuario
		fields = ['first_name','last_name']

class UsuarioSerializer(serializers.ModelSerializer):
	#adoptante_usuario = SolicitudSerializer(source="adoptante",many=True, read_only=True)
	amigos_usuario = AmigosSerializer(source="contribuidor", many=True, read_only=True)
	class Meta:
		model = Usuario
		fields = ['id','username','first_name','last_name','email','is_active','direccion','telefono','amigos_usuario']
	