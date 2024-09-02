from django.db import models
from django.contrib.postgres.fields import ArrayField
import uuid
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)

    product_name = models.CharField(max_length=100, blank=False)
    price = models.FloatField(blank=False, default=0.0)
    description = models.TextField()
    ref = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    discount = models.FloatField(blank=True, default=0.0)


class Order(models.Model):
    ORDER_STATUS = (
        ("TRANSACTION_SUCCESS", "Success"),
        ("TRANSACTION_CLOSED", "Close"),
        ("TRANSACTION_FINISHED", "Finish"),
        ("TRANSACTION_CANCELED", "Cancel"),
        ("TRANSACTION_FAILED", "Fail"),
        ("TRANSACTION_SUBMITTED", "Submit")
    )
    PAY_TYPE = (
        ("credit", "CreditCard"),
        ("stripe", "Stripe"),
        ("paypal", "Paypal"),
        ("check", "Check"),
    )

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    order_number = models.TextField(blank=False)
    order_status = models.CharField("Order Status",choices=ORDER_STATUS, default="TRANSACTION_SUBMITTED", max_length=30)
    transaction_number = models.CharField("Transaction Number",max_length=100, unique=True, null=True, blank=True),
    pay_type = models.CharField("Pay Type",choices=PAY_TYPE, default="stripe", max_length=12)
    products = ArrayField(models.UUIDField(), blank=False, default=list)
    # products = models.UUIDField()
    coupon = models.CharField(max_length=50, blank=True)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)

    order_number = models.TextField(blank=False)

    price = models.FloatField(blank=False, default=0.0)
    card_number = models.CharField(max_length=50)
    token = models.TextField()

    name = models.CharField(max_length=50)

    phone = models.CharField(max_length=20)
    email = models.EmailField()
    billing_address = models.TextField()
    billing_zipcode = models.CharField(max_length=10)
    billing_city = models.CharField(max_length=50)
    billing_state = models.CharField(max_length=20)

    shipping_address = models.TextField()
    shipping_zipcode = models.CharField(max_length=10)
    shipping_city = models.CharField(max_length=50)
    shipping_state = models.CharField(max_length=20)


class Cart(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    products = ArrayField(models.UUIDField(), blank=False, default=list)
    # products = models.UUIDField()


class PopularSearchWords(models.Model):
    keywords = models.CharField("Popular Keywords", default="", max_length=20)
    index = models.IntegerField("Index", default=0)
    add_time = models.DateTimeField("Add Time", default=datetime.datetime.now)

    class Meta:
        verbose_name = 'Popular Searches'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords

