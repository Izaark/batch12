from rest_framework import filters
from rest_framework import viewsets
from .serializers import InfanteSerializer
from .models import Infante

class InfanteViewSet(viewsets.ModelViewSet):
	queryset = Infante.objects.all()
	serializer_class = InfanteSerializer