from django.db import models


class WeeklyDeal(models.Model):
    year = models.CharField(max_length=30, blank=False)
    make = models.CharField(max_length=100, blank=False)
    model = models.CharField(max_length=100, blank=False)
    trim = models.CharField(max_length=100)
    image = models.TextField()

    msrp = models.CharField(max_length=100, blank=False)
    monthly_payment = models.CharField(max_length=100, blank=False)
    drive_off = models.CharField(max_length=100, blank=False, default='0')
    other_info = models.CharField(max_length=100)

    # week = models.CharField(max_length=5)
    promotion_year = models.CharField(max_length=30, blank=False)

    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    current = models.CharField(max_length=5, blank=False, default='0')

    entered_date = models.DateTimeField(blank=False, auto_now_add=True)
    modified_date = models.DateTimeField(blank=False, auto_now_add=True)


class PastDeal(models.Model):
    year = models.CharField(max_length=30, blank=False)
    make = models.CharField(max_length=100, blank=False)
    model = models.CharField(max_length=100, blank=False)
    trim = models.CharField(max_length=100)
    image = models.TextField()

    msrp = models.CharField(max_length=100, blank=False)
    monthly_payment = models.CharField(max_length=100, blank=False)
    drive_off = models.CharField(max_length=100, blank=False, default='0')
    other_info = models.CharField(max_length=100)

    # week = models.CharField(max_length=5)
    promotion_year = models.CharField(max_length=30, blank=False)

    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    current = models.CharField(max_length=5, blank=False, default='0')

    entered_date = models.DateTimeField(blank=False, auto_now_add=True)
    modified_date = models.DateTimeField(blank=False, auto_now_add=True)

