from django.conf.urls import url,include
from .views import *


urlpatterns = [
    url(r'^nuevo/', InfanteCreateView.as_view(), name='infante_crear'),
    url(r'^lista/', InfanteListView.as_view(), name='infante_listar'),
    url(r'^editar/(?P<pk>\d+)/$',InfanteUpdateView.as_view(), name='infante_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',InfanteDeleteView.as_view(), name='infante_eliminar'),
    
]
