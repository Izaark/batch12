from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views_apiset import SolicitudViewSet
router = DefaultRouter()
router.register(r'',SolicitudViewSet)

urlpatterns = [
	url(r'^listado_api_adoptante/', include(router.urls)),
	#url(r'^listado_api_user_filter/', UsuarioList.as_view()),
	
]