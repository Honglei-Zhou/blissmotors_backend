from rest_framework import serializers
from .models import Product, Order, Payment
import uuid


class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    description = serializers.CharField(required=True)
    discount = serializers.FloatField(required=False)
    ref = serializers.UUIDField(required=False)

    def create(self, validated_data):

        price = validated_data.get('price')
        product_name = validated_data.get('product_name')
        description = validated_data.get('description')
        discount = validated_data.get('discount')
        # ref = serializers.UUIDField()

        # product = Product(product_name=product_name, price=price, description=description, discount=discount)
        print(price)
        print(product_name)

        product = Product()
        product.price = price
        product.product_name = product_name
        product.description = description
        product.ref = uuid.uuid4()
        print(product)

        product.save()

        if discount:
            product.discount = discount
        return product

    class Meta:
        model = Product
        fields = ('id', 'product_name', 'price', 'description', 'discount', 'ref')
        # fields = ('id', 'source')


class ProductListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    description = serializers.CharField(required=True)
    discount = serializers.FloatField(required=False, default=0.0)
    ref = serializers.UUIDField()

    class Meta:
        model = Product
        fields = ('id', 'product_name', 'price', 'description', 'discount', 'ref')


class OrderSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(required=True)
    # products = serializers.ListField(
    #     child=serializers.UUIDField()
    # )
    products = serializers.UUIDField()

    def create(self, validated_data):

        order_number = validated_data.get('order_number')
        products = validated_data.get('products')

        order = Order(order_number=order_number, products=products)
        order.save()

        return order

    class Meta:
        model = Order
        fields = ('id', 'order_number', 'products')


class OrderListSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(required=True)
    # products = serializers.ListField(
    #     child=serializers.UUIDField()
    # )
    products = serializers.UUIDField()

    class Meta:
        model = Order
        fields = ('id', 'order_number', 'products')


class PaymentSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    card_number = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    name = serializers.CharField(required=True)

    phone = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    billing_address = serializers.CharField(required=True)
    billing_zipcode = serializers.CharField(required=True)
    billing_city = serializers.CharField(required=True)
    billing_state = serializers.CharField(required=True)

    shipping_address = serializers.CharField(required=True)
    shipping_zipcode = serializers.CharField(required=True)
    shipping_city = serializers.CharField(required=True)
    shipping_state = serializers.CharField(required=True)

    def create(self, validated_data):

        order_number = validated_data.get('order_number')
        price = validated_data.get('price')
        card_number = validated_data.get('card_number')
        token = validated_data.get('token')

        name = validated_data.get('name')
        phone = validated_data.get('phone')
        email = validated_data.get('email')

        billing_address = validated_data.get('billing_address')
        billing_zipcode = validated_data.get('billing_zipcode')
        billing_city = validated_data.get('billing_city')
        billing_state = validated_data.get('billing_state')

        shipping_address = validated_data.get('shipping_address')
        shipping_zipcode = validated_data.get('shipping_zipcode')
        shipping_city = validated_data.get('shipping_city')
        shipping_state = validated_data.get('shipping_state')

        payment = Payment()
        payment.order_number = order_number
        payment.price = price
        payment.card_number = card_number
        payment.token = token
        payment.name = name
        payment.phone = phone
        payment.email = email

        payment.billing_address = billing_address
        payment.billing_zipcode = billing_zipcode
        payment.billing_city = billing_city
        payment.billing_state = billing_state

        payment.shipping_address = shipping_address
        payment.shipping_zipcode = shipping_zipcode
        payment.shipping_city = shipping_city
        payment.shipping_state = shipping_state

        payment.save()

        return payment
    
    class Meta:
        model = Payment
        fields = ('id', 'order_number', 'price', 'card_number', 'token', 'name', 'phone', 'email',
                  'billing_address', 'billing_zipcode', 'billing_city', 'billing_state',
                  'shipping_address', 'shipping_zipcode', 'shipping_city', 'shipping_state')


class PaymentListSerializer(serializers.ModelSerializer):
    order_number = serializers.CharField(required=True)
    price = serializers.FloatField(required=True)
    card_number = serializers.CharField(required=True)
    token = serializers.CharField(required=True)

    name = serializers.CharField(required=True)

    phone = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    billing_address = serializers.CharField(required=True)
    billing_zipcode = serializers.CharField(required=True)
    billing_city = serializers.CharField(required=True)
    billing_state = serializers.CharField(required=True)

    shipping_address = serializers.CharField(required=True)
    shipping_zipcode = serializers.CharField(required=True)
    shipping_city = serializers.CharField(required=True)
    shipping_state = serializers.CharField(required=True)

    class Meta:
        model = Payment
        fields = ('id', 'order_number', 'price', 'card_number', 'token', 'name', 'phone', 'email',
                  'billing_address', 'billing_zipcode', 'billing_city', 'billing_state',
                  'shipping_address', 'shipping_zipcode', 'shipping_city', 'shipping_state')
