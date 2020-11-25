from django.contrib import admin
from .models import Product, Order, OrderDetail


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'stock']
    list_display = ('id', 'name', 'price', 'stock')    


class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 3


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'date_time', 'get_total', 'get_total_usd']
    inlines = [OrderDetailInline, ]
    list_display = ('id', 'date_time', 'get_total', 'get_total_usd')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)