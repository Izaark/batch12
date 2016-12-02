from rest_framework import serializers
from .models import Direccion,Colonia
from usuario.serializers import UsuarioSerializer
from adoptante.serializers import PersonaSerializer

class DireccionSerializer(serializers.ModelSerializer):
	direccion_usuario = UsuarioSerializer(many = True, read_only= True)
	persona_direccion = PersonaSerializer(many=True, read_only=True)
	class Meta:
		model = Direccion
		fields = ['id','slug','calle','numero_interior','numero_exterior','direccion_usuario','persona_direccion']

class ColoniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colonia
        fields = ["codigo_postal", "nombre", "municipio", "ciudad","estado","pais"]