from django.shortcuts import render, get_object_or_404, redirect
from .forms import CartAddProductForm
from django.views.generic import View
from .cart import Cart
from tienda.models import Producto

class Agregar(View):
	def post(self,request,producto_id):
		cart = Cart(request)
		producto = get_object_or_404(Producto,id=producto_id)
		form = CartAddProductForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			cart.add(producto=producto,
				quantity=cd['quantity'],
				update_quantity=cd['update'])
		return redirect('tienda:tienda')

class Remove(View):
	def get(self,request,producto_id):
		cart = Cart(request)
		producto = get_object_or_404(Producto,id=producto_id)
		cart.remove(producto)
		return redirect('cart:cart_detail')

class Detalle(View):
	def get(self,request):
		cart = Cart(request)
		return render(request,'cart/detalle.html',{'cart':cart})
