from decimal import Decimal
from django.conf import settings
from productos.models import Producto

class Cart(object):
	def __init__(self,request):
		"""
		Inicializamos el carrito de compras
		"""
		self.session = request.session
		self.cart = self.session.get(settings.CART_SESSION_ID)
		if not self.cart:
			#Guardar el carrito vacio en la session
			self.cart = self.session[settings.CART_SESSION_ID] = {}

	def add(self, producto, quantity=1, update_quantity=False):
		"""
		Agregamos un producto nuevo al carrito o lo actualizamos
		"""
		producto_id = str(producto.id)
		if producto_id not in self.cart:
			self.cart[producto_id] = {
				'quantity':0,
				'precio':str(producto.precio)
			}
		if update_quantity:
			self.cart[producto_id]['quantity'] += quantity
		else:
			self.cart[producto_id]['quantity'] = quantity
		self.save()
	def save(self):
		#Actualizamos el carrito en la session
		self.session[settings.CART_SESSION_ID] = self.cart
		#marcamos la session como modificada para asegurarnos que si guardamos
		self.session.modified = True

	def remove(self,producto):
		"""
		Eliminamos un producto del carrito
		"""
		producto_id = str(producto.id)
		if producto_id in self.cart:
			del self.cart[producto_id]
			self.save()

	def __iter__(self):
		"""
		Iterar en los elementos del carrito y traer
		 los productos de la base de datos
		"""
		producto_ids = self.cart.keys()
		#traer el producto y agregarlo
		tienda = Producto.objects.filter(id__in=producto_ids)
		for producto in tienda:
			self.cart[str(producto.id)]['producto'] = producto

		for item in self.cart.values():
			item['precio'] = Decimal(item['precio'])
			item['precio_total'] = item['precio'] * item['quantity']
			yield item

	def __len__(self):
		"""
		Cuenta todos los items en el carrito
		"""
		return sum(item['quantity'] for item in self.cart.values())

		"""
		suma = 0
		for item in self.cart.values():
			suma = sum(item['quantity'])
		return suma
		"""

	def get_precio_total(self):
		return sum(Decimal( item['precio']) * item['quantity'] for item in self.cart.values() )

	def clear(self):
		#borrar el carrita de las esion de usuario
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True