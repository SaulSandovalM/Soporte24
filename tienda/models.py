from django.db import models

class Producto(models.Model):
    imagen = models.FileField(upload_to='tienda/%Y/%m/%d/', null=True, blank=True)
    nombre = models.CharField(max_length=140)
    precio = models.FloatField()
