from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='producto'), # index del cliente
    path('nuevo', views.guardar, name='crear_producto'),
    
]
