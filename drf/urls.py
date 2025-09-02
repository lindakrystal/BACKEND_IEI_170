"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app_libreria.views import (
    inicio, lista_libros, lista_lectores, lista_bibliotecas, lista_autores,
    lista_nacionalidades, lista_comunas, lista_direcciones, lista_prestamos
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app_libreria.urls')),  # Incluye las URLs de tu app
   path('inicio/', inicio, name='inicio'),
   path('libros/', lista_libros, name='lista_libros'),
    path('lectores/', lista_lectores, name='lista_lectores'),
    path('bibliotecas/', lista_bibliotecas, name='lista_bibliotecas'),
    path('autores/', lista_autores, name='lista_autores'),
    path('nacionalidades/', lista_nacionalidades, name='lista_nacionalidades'),
    path('comunas/', lista_comunas, name='lista_comunas'),
    path('direcciones/', lista_direcciones, name='lista_direcciones'),
    path('prestamos/', lista_prestamos, name='lista_prestamos'),
]