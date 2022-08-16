from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='clientes'), # index del cliente
    path('nuevo/', views.guardar, name='crear_cliente'),
    
]
