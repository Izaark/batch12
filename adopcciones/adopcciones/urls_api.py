from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
   url(r'^direcciones/', include('direccion.urls_api')),
   url(r'^usuarios/', include('usuario.urls_api')),
   url(r'^adoptantes/', include('adoptante.urls_api')),
   url(r'^infantes/', include('infante.urls_api')),
]
