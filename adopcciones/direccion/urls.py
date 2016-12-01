from django.conf.urls import url
from .views import DireccionListView,DireccionCreateView,DireccionUpdateView,DireccionDeleteView

urlpatterns = [

url(r'^lista/', DireccionListView.as_view(), name='direccion_listar'),
url(r'^nueva_direccion/', DireccionCreateView.as_view(), name='direccion_crear'),
url(r'^editar/(?P<pk>\d+)/$',DireccionUpdateView.as_view(), name='direccion_editar'),
url(r'^eliminar/(?P<pk>\d+)/$',DireccionDeleteView.as_view(), name='direccion_eliminar'),
]