from django.conf.urls import url,include
from django.contrib.auth.views import login,logout_then_login
from django.contrib import admin
from adopcciones import urls_api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	# url(r'^login/',login,{'template_name':'index.html'}, name='login'),
	# url(r'^logout/',logout_then_login, name='logout'),
 	url(r'^api/v1/', include(urls_api)),
    
    url(r'^direcciones/', include("direccion.urls", namespace='direcciones')),
    url(r'^usuarios/', include("usuario.urls", namespace='Usuario')),
    url(r'^adopcciones/', include("adoptante.urls",namespace='adoptante')),
    url(r'^infantes/', include("infante.urls",namespace='infante')),
]
