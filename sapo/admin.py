from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Product)
admin.site.register(Customer)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product','order_id', 'order', 'quantity', 'date_added']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','code','customer', 'date_created', 'complete']
    
  