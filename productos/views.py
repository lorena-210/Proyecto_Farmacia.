from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from .models import Producto
from .models import TipoProducto


def index( request ):
    return render(request, 'index.html')

def base( request ):
    return render(request, 'base.html')

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            productos = Producto.objects.all()
            return redirect(request, 'productos/listar_productos.html')
    else: 
        form = ProductoForm()
        tipos = TipoProducto.objects.all()
    return render(request, 'productos/registrar_producto.html', {'form': form, 'tipos': tipos})

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
        tipos = TipoProducto.objects.all()
    return render(request, 'productos/modificar_producto.html', {'form': form, 'tipos': tipos})