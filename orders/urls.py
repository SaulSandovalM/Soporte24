from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^create/$',views.CreateOrder.as_view(), name="create"),
]	
