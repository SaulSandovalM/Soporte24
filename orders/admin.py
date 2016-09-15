from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['producto']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','first_name','last_name','email','fecha','paid']
	list_filter = ['paid','fecha']
	inlines = [OrderItemInline]
admin.site.register(Order,OrderAdmin)
