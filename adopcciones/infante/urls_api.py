from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views_apiset import InfanteViewSet
router = DefaultRouter()
router.register(r'',InfanteViewSet)

urlpatterns = [
	url(r'^listado_api_infantes/', include(router.urls)),
]