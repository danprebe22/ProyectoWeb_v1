from django.conf.urls import include, url, re_path

from MillenialPet.views import index, packs, productos, promociones, unete, contacto, acercade

from django.contrib import admin
from django.urls import path, re_path
from MillenialPet import views
from django.contrib.auth.views import password_reset, password_reset_done,password_reset_confirm,password_reset_complete
from django.contrib.auth import login

urlpatterns = [

    #path('admin/', admin.site.urls),

    path('', views.login, name='login'),
    path('productos/',views.productos,name='productos'),
    path('registro/',views.registro,name='registrarse'),
    path('citas/',views.citas,name="citas"),
    path('citas/agendarcita/',views.agendar_cita,name="agendar"),
    path('error404/',views.error, name="error"),
    path('index/', views.index, name="index"),

    path('promociones/', views.promociones(), name="promociones")
    path('unete/', views.unete, name="unete"),
    path('packs/', views.packs, name="packs"),

    """""  
    #url('index/', index, name='index'),
    #url('packs/', packs, name='packs'),
    #url('productos/', productos, name='productos'),
    #url('promociones/', promociones, name='promociones'),
    #url('unete/', unete, name="unete"),
    url('contacto/', contacto, name="contacto"),
    url('acercade/', acercade, name="acercade")
    """

]