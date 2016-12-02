from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
   url(r'^direcciones/', include('direccion.urls_api')),
   url(r'^usuarios/', include('usuario.urls_api')),
   url(r'^adoptantes/', include('adoptante.urls_api')),
   url(r'^auth/', obtain_jwt_token),
   url(r'^infantes/', include('infante.urls_api')),
]
