from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets
from .serializers import *
from .models import Solicitud,Persona

class SolicitudViewSet(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = PersonaSerializer