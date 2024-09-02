from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import datetime

class Customer(models.Model):
    pass


class Dealer(models.Model):
    pass


class Profile(models.Model):
    id = models.AutoField(primary_key=True)

    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING, blank=True, null=True)

    company_name = models.TextField()
    email = models.EmailField()
    office_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)

    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    address_3 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    date_entered = models.DateTimeField(blank=False, auto_now_add=True)
    date_modified = models.DateTimeField(blank=False, auto_now_add=True)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)

    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField()
    office_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)

    date_entered = models.DateTimeField(blank=False, auto_now_add=True)
    date_modified = models.DateTimeField(blank=False, auto_now_add=True)


class RegistrationCode(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False)
    code = models.CharField(max_length=16, blank=False)
    date_entered = models.DateTimeField(blank=False, auto_now_add=True)
    date_modified = models.DateTimeField(blank=False, auto_now_add=True)


class Inventory(models.Model):

    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)
    year = models.CharField(max_length=30)
    msrp = models.CharField(max_length=100)
    sale_price = models.CharField(max_length=100)
    rebate = models.CharField(max_length=100)
    res = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    yearly_mileage = models.CharField(max_length=100)
    money_factor = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)

    date_entered = models.DateTimeField(blank=False, auto_now_add=True)
    date_modified = models.DateTimeField(blank=False, auto_now_add=True)

    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING)
