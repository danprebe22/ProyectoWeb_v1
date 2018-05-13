"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from MillenialPet import views
from django.contrib.auth.views import password_reset, password_reset_done,password_reset_confirm,password_reset_complete
from django.contrib.auth import login
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.login, name='login'),

    path('registro/', views.registro, name='registrarse'),
    path('citas/', views.citas, name="citas"),
    path('citas/agendarcita/', views.agendar_cita, name="agendar"),
    path('404/', views.error, name="error"),
    path('contraseña/', views.contraseña, name="contraseña"),
    path('iniciarSesión/', views.iniciarSesión, name="iniciarSesión"),

    path('index/', views.index, name="index"),

    path('packs/', views.packs, name="packs"),
    path('productos/', views.productos, name='productos'),
    path('promociones/', views.promociones, name="promociones"),
    path('unete/', views.unete, name="unete"),
    path('contacto/', views.contacto, name='contacto'),
    path('acercade/', views.acercade, name="acercade"),
]
