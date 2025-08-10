from django.contrib.auth.models import User, Group
from .models import *
from django.db import models
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product

        fields = ['id', 'name', 'code', 'category', 'brand', 'stock', 'qr_code', 'mass', 'image', 'tag', 'import_price', 'wholesale_price', 'retail_price', 'description', 'color', 'unit', 'status', 'tax']
        


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='orders-detail'
    )

    class Meta:
        model = Customer
        fields = ['id', 'name', 'code', 'sex', 'date_of_birth', 'email', 'employee_care', 'phone', 'address', 'debit', 'tag', 'segment', 'tax_code', 'website', 'description', 'price_policy', 'customer_discount', 'payment','orders']


    

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = Order
        fields = ['id','code','customer', 'date_created', 'complete', 'pay', 'price_policy','sale_location','employee_sale','ship_date','source','chanel','path','reference','ship_address','total']


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = OrderItem
        fields = ['id','order', 'product', 'quantity', 'date_added']
    
    # Map the foreign key fields to the serializer fields  
class ImportSerializer(serializers.Serializer):

       file = serializers.FileField()