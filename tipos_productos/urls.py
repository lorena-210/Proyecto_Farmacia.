from django.urls import path
from . import views

urlpatterns = [

    path('agregar/', views.agregar_tipo_producto, name='agregar_tipo_producto'),
    path('mostrar_tipos/', views.mostrar_tipos_productos, name='mostrar_tipos_productos'),
]