from django.db import models


class Campaign(models.Model):
    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20)

    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    address_3 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    source = models.CharField(max_length=255)

    date_entered = models.DateTimeField(blank=False, auto_now_add=True)
    date_modified = models.DateTimeField(blank=False, auto_now_add=True)


class Inquiry(models.Model):
    id = models.AutoField(primary_key=True)

    source = models.CharField(max_length=50, blank=False)

    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=False)

    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    address_3 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10, blank=False)

    message = models.TextField()
    year = models.CharField(max_length=30, blank=False)
    make = models.CharField(max_length=100, blank=False)
    model = models.CharField(max_length=100, blank=False)
    trim = models.CharField(max_length=100)

    price = models.CharField(max_length=30)

    cartype = models.CharField(max_length=100)
    contacttype = models.CharField(max_length=30)






