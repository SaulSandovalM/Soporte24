from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Producto
from cart.forms import CartAddProductForm

class Lista(View):
    def get(self, request):
        productos = Producto.objects.all()
        template_name = 'tienda/lista.html'
        context = {
        'productos':productos
        }
        return render(request, template_name, context)

class Detalle(View):
    def get(self, request, producto_id):
        template_name = 'tienda/detalle.html'
        producto = get_object_or_404(Producto,id=producto_id)
        form = CartAddProductForm()
        context = {
        'producto':producto,
        'form':form
        }
        return render(request, template_name, context)
