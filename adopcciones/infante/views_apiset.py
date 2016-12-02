from rest_framework import filters
from rest_framework import viewsets
from .serializers import InfanteSerializer
from .models import Infante
from .permissions import ApiUserPermissions

class InfanteViewSet(viewsets.ModelViewSet):
	queryset = Infante.objects.all()
	serializer_class = InfanteSerializer
	filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
	filter_fields = ('sex',)
	search_fields = ('name','age',)
	#permission_classes = (ApiUserPermissions,)