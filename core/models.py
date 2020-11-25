from django.db import models
from .cotizacion_dolar import Cotizacion


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    date_time = models.DateTimeField('date order', auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.date_time)

    def get_total(self):
        total = 0
        for od in self.orderdetail_set.all():
            total = total + (od.product.price * od.quantity)
        formatted_float = "{:.2f}".format(total)
        return formatted_float

    def get_total_usd(self):
        cotizacion = Cotizacion.get_cotizacion_dolar_blue()
        total_usd = 0
        total_usd = float(self.get_total()) / cotizacion
        formatted_float = "{:.2f}".format(total_usd)
        return formatted_float

    def delete(self, *args, **kwargs):
        for od in self.orderdetail_set.all():
            od.product.stock = od.product.stock + od.quantity
            od.product.save()
        super().delete(*args, **kwargs)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super(OrderDetail, self).__init__(*args, **kwargs)
        self.old_quantity = self.quantity

    def __str__(self):
        return "Order: " + str(self.order) + " product: " + self.product.name

    def save(self, *args, **kwargs):
        if self.id:
            diff_quantity = self.old_quantity - self.quantity
            self.product.stock = self.product.stock + diff_quantity
            self.product.save()
        else:
            self.product.stock = self.product.stock - self.quantity
            self.product.save()

        super().save(*args, **kwargs)