from django.urls import path
from . import views

urlpatterns = [
    path("loginCliente",views.loginCliente),
    path("loginGuia",views.loginGuia),
    path("registroCliente",views.registrarCliente),
    path("registroGuia",views.registrarGuia)
]