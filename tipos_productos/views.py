from django.shortcuts import render, redirect, get_object_or_404
from .forms import TipoProductoForm
from .models import TipoProducto


#def listar_tipos_productos(request):
#    tipos_productos = TipoProducto.objects.all()
#    return render(request, 'tipos_productos/listar_tipos_productos.html', {'tipos_productos': tipos_productos})

def agregar_tipo_producto(request):
    if request.method == 'POST':
        form = TipoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_tipos_productos')
    else:
        form = TipoProductoForm()

    return render(request, 'tipos/agregar_tipo_producto.html', {'form': form})

def mostrar_tipos_productos(request):
    tipos_productos = TipoProducto.objects.all()
    return render(request, 'tipos/mostrar_tipos_productos.html', {'tipos_productos': tipos_productos})

def modificar_tipo_producto(request, tipo_producto_id):
    tipo_producto = get_object_or_404(TipoProducto, id=tipo_producto_id)

    if request.method == 'POST':
        form = TipoProductoForm(request.POST, instance=tipo_producto)
        if form.is_valid():
            form.save()
            return redirect('mostrar_tipos_productos')
    else:
        form = TipoProductoForm(instance=tipo_producto)

    return render(request, 'tipos/modificar_tipo_producto.html', {'form': form, 'tipo_producto': tipo_producto})

# def eliminar_tipo_producto(request, tipo_producto_id):
#     tipo_producto = get_object_or_404(TipoProducto, id=tipo_producto_id)
    
#     if request.method == 'POST':
#         tipo_producto.delete()
#         return redirect('mostrar_tipos_productos')
    
#     return render(request, 'tipos/eliminar_tipo_producto.html', {'tipo_producto': tipo_producto})

# # En tu archivo views.py

from django.shortcuts import get_object_or_404, redirect

def eliminar_tipo_producto(request, tipo_producto_id):
    tipo_producto = get_object_or_404(TipoProducto, id=tipo_producto_id)
    
    if request.method == 'POST':
        tipo_producto.delete()
        return redirect('mostrar_tipos_productos')  # Reemplaza con tu URL de mostrar tipos de productos
    
    return render(request, 'tipos/eliminar_tipo_producto.html', {'tipo_producto': tipo_producto})
