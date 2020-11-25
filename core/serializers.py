from rest_framework import serializers
from .models import Product, Order, OrderDetail


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock']


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['quantity', 'product']


class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True, read_only=True, source='orderdetail_set')
    
    class Meta:
        model = Order
        fields = ['id', 'date_time', 'get_total', 'get_total_usd', 'details']