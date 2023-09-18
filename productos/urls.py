from django.urls import path
from .views import listar_productos, registrar_producto, index, modificar_producto, base


urlpatterns = [
    path('base/', base, name='hogar'),
    path('', index, name='home'),
    path('listar/', listar_productos, name='listar_productos'),
    path('registrar/', registrar_producto, name='registrar_producto'),
    path('modificar/<id>/', modificar_producto, name='modificar_producto'),

]

