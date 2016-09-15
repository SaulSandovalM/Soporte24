from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.Lista.as_view(), name="tienda"),
    url(r'^(?P<producto_id>\d+)/$', views.Detalle.as_view(), name="detalle"),
]
