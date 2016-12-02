from rest_framework import serializers
from .models import Persona,Solicitud
from usuario.serializers import UsuarioSerializer
from infante.serializers import InfanteSerializer
class PersonaSerializer(serializers.ModelSerializer):
	usuario_persona = UsuarioSerializer(many=True,read_only=True)
	persona_infante = InfanteSerializer(many=True, read_only=True)
	class Meta:
		model = Persona
		fields = ['name','last_name','email','usuario','usuario_persona','persona_infante']

class SolicitudSerializer(serializers.ModelSerializer):
	persona_solicitud = PersonaSerializer(many=True,read_only=True)
	class Meta:
		model = Solicitud
		fields = ['razones','persona_solicitud']