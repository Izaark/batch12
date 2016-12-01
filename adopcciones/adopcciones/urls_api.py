from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
   url(r'^direcciones/', include('direccion.urls_api')),
   url(r'^usuarios/', include('usuario.urls_api')),
]
