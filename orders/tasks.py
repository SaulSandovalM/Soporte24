from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
	"""
	Esta tarea enviará un email de que la orden fue creada con éxito
	"""
	order=Order.objects.get(id=order_id)
	subject='Your order #{}'.format(order.id)
	message= 'Querido {},\n\nHemos recibido tu orden No. {}'.format(order.first_name,order.id)
	mail_sent = send_mail(subject, message, 'saul_watch_dogs@outlook.com',[order.email])
	return mail_sent
