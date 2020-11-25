from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order, OrderDetail
from .serializers import ProductSerializer, OrderSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['put'], detail=True)
    def stock(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        product.stock = request.data.get("stock")
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def valid_deatils(self):
        pass

    def create(self, request):
        errors = []
        products = []
        duplicated_products = []
        product_in_zero = []
        product_stock_zero = []
        for data in request.data:
            product = Product.objects.get(pk=data.get('product'))
            stock = product.stock - data.get('quantity')
            if stock < 0:
                product_stock_zero.append(data.get('product'))

            if data.get('quantity') == 0:
                product_in_zero.append(data.get('product'))

            if data.get('product') in products:
                duplicated_products.append(data.get('product'))
            else:
                products.append(data.get('product'))

        if duplicated_products:
            errors.append('Duplicated product:' + str(duplicated_products))

        if product_in_zero:
            errors.append('Product quantity in zero:' + str(product_in_zero))

        if product_stock_zero:
            errors.append('Product stock zero:' + str(product_stock_zero))

        if errors:
            content = {'error': str(errors)}
            status_response = status.HTTP_400_BAD_REQUEST
        else:
            order = Order()
            order.save()
            for data in request.data:
                order_detail = OrderDetail()
                order_detail.order = order
                order_detail.quantity = data.get('quantity')
                order_detail.product = Product.objects.get(pk=data.get('product'))
                order_detail.save()
            status_response = status.HTTP_201_CREATED
            content = OrderSerializer(order).data

        return Response(content, status=status_response)


    def update(self, request, pk):
        order = Order.objects.get(pk=pk)
        for data in request.data['details']:
            order_details = OrderDetail()
            for od in order.orderdetail_set.all():
                if od.product.pk == data.get('product'):
                    order_details = od
            order_details.product = Product.objects.get(pk=data.get('product'))
            order_details.quantity = data.get('quantity')
            order_details.save()

        content = OrderSerializer(order).data
        return Response(content)