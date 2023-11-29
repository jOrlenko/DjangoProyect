"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Aqui importamos la url para poder mostrar las imagenes.
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # hemos creado un urls.py en la app para administrar las vistas, 
    # y desde alli las importamos al path del proyecto 
    # Esto es por si tenemos mas app que el urlpatterns no sea gigantesco
    path('', include('ProyectoFinalApp.urls')),
    path('servicios/', include('ServiciosApp.urls')),
    path('blog/', include('BlogApp.urls')),
    path('contacto/', include('ContactoApp.urls')),
    path('tienda/', include('TiendaApp.urls')),
]


# Aquí asignamos la direccion para mostrar las medias
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)