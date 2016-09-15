from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.Detalle.as_view(), name="cart_detail"),
    url(r'^add/(?P<producto_id>\d+)/$', views.Agregar.as_view(), name="cart_add"),
    url(r'^remove/(?P<producto_id>\d+)/$', views.Remove.as_view(), name="cart_remove")
]
