from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import OrderItem, Order
from .tasks import order_created

class CreateOrder(View):
	def get(delf, request):
		form = OrderCreateForm()
		template_name = 'orders/create.html'
		context = {
		'form':form,
		'cart':Cart(request)
		}
		return render(request, template_name, context)

	def post(self, request):
		cart = Cart(request)
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(
					order=order,
					product=item['product'],
					price=item['price'],
					quantity=item['quantity']
					)
			#borrar carrito
			cart.clear()
			#enviaremos una tarea asíncrona a celery
			order_created.delay(order.id)

			#orden para paypal
			request.session['order_id']=order.id
			return redirect(reverse('payment:process'))
		else:
			cart=Cart(request)
			form=OrderCreateForm(request.POST)
			template='orders/create.html'
			context={
			'cart':cart,
			'form':form
			}
		return render(request,template,context)
