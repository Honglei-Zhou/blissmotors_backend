from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    source_url = models.TextField(blank=True, default='')
    description = models.CharField(max_length=255)

    logo = models.TextField(blank=True, default='')

    # class Meta:
    #     managed = False
    #     db_table = 'car_make'

    def __str__(self):
        return self.name


class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    description = models.CharField(max_length=255)
    referer = models.TextField(blank=True, default='')

    logo = models.TextField(blank=True, default='')

    # class Meta:
    #     managed = False
    #     db_table = 'car_model'

    def __str__(self):
        return _('%s %s') % (self.make, self.name)


class CarType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    logo = models.TextField(blank=True, default='')

    # class Meta:
    #     managed = False
    #     db_table = 'car_type'

    def __str__(self):
        return self.name


class CarTrim(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cartype = models.CharField(max_length=100)

    trim = models.CharField(max_length=100)
    year = models.CharField(max_length=30)

    style = models.TextField()

    mpg = models.CharField(max_length=50)
    msrp = models.CharField(max_length=100)

    seats = models.IntegerField()

    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=255)
    drivetrain = models.CharField(max_length=100)

    source_url = models.TextField()
    specs_url = models.TextField()

    # class Meta:
    #     managed = False
    #     db_table = 'car_trim'

    def __str__(self):
        return _("%s %s %s %s") % (self.year, self.make, self.model, self.trim)


class CarSpecs(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cartype = models.CharField(max_length=100)

    trim = models.CharField(max_length=100)
    year = models.CharField(max_length=30)

    style = models.TextField()

    seats = models.IntegerField()
    doors = models.IntegerField()
    mpg = models.CharField(max_length=30)

    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=255)
    drivetrain = models.CharField(max_length=100)
    warranty = models.CharField(max_length=255)

    source_url = models.TextField()

    # class Meta:
    #     managed = False
    #     db_table = 'car_specs'

    def __str__(self):
        return _("%s %s %s %s") % (self.year, self.make, self.model, self.trim)


class CarImage(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cartype = models.CharField(max_length=100)

    year = models.CharField(max_length=30)

    source_url = models.TextField()
    path_key = models.TextField()
    path_value = models.TextField()
    path_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cars_carimage'


class CarImagePath(models.Model):
    id = models.AutoField(primary_key=True)

    path_key = models.TextField()
    path_dest = models.TextField()

    # class Meta:
    #     managed = False
    #     db_table = 'car_image_path'


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cartype = models.CharField(max_length=100)
    year = models.CharField(max_length=30)

    competitors = models.TextField()

    mpg = models.CharField(max_length=50)
    msrp = models.CharField(max_length=100)

    description = models.TextField()
    source_url = models.TextField()
    shopping_url = models.TextField()
    image = models.TextField()

    features = models.TextField()

    msrp_min = models.IntegerField()
    msrp_max = models.IntegerField()

    category = models.CharField(max_length=50)
    payment = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cars_car'

    def __str__(self):
        return _("%s %s %s %s") % (self.year, self.make, self.model, self.trim)


class CarInventory(models.Model):

    id = models.AutoField(primary_key=True)

    year = models.CharField(max_length=30)
    make = models.CharField(max_length=100)

    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)
    msrp = models.FloatField(blank=False, default=0.0)
    sale_price = models.FloatField(blank=False, default=0.0)
    rebate = models.FloatField(blank=False, default=55.0)
    res = models.FloatField(blank=False, default=55.0)
    term = models.FloatField(blank=False, default=36.0)
    yearly_mileage = models.FloatField(blank=False, default=10000.0)
    money_factor = models.FloatField(blank=False, default=0.0002)

    deposit = models.CharField(max_length=50)
    due = models.CharField(max_length=50)
    payment = models.FloatField(blank=False, default=0.0)

    invoice = models.FloatField()
    residual = models.FloatField()
    comment = models.TextField()

    image = models.CharField(max_length=100)
    cartype = models.CharField(max_length=100)

    competitors = models.TextField()

    dealer_id = models.TextField(default='Bliss Motors')
    car_id = models.TextField(default='Car ID')


class MoneyFactor(models.Model):

    id = models.AutoField(primary_key=True)

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)

    mo_24 = models.FloatField(blank=False, default=0.0)
    mo_27 = models.FloatField(blank=False, default=0.0)
    mo_30 = models.FloatField(blank=False, default=0.0)
    mo_33 = models.FloatField(blank=False, default=0.0)
    mo_36 = models.FloatField(blank=False, default=0.0)
    mo_39 = models.FloatField(blank=False, default=0.0)
    mo_42 = models.FloatField(blank=False, default=0.0)
    mo_45 = models.FloatField(blank=False, default=0.0)
    mo_48 = models.FloatField(blank=False, default=0.0)
    mo_51 = models.FloatField(blank=False, default=0.0)
    mo_54 = models.FloatField(blank=False, default=0.0)
    mo_57 = models.FloatField(blank=False, default=0.0)
    mo_60 = models.FloatField(blank=False, default=0.0)

    tier_4 = models.FloatField(blank=False, default=0.0)
    tier_5 = models.FloatField(blank=False, default=0.0)
    tier_6 = models.FloatField(blank=False, default=0.0)
    tier_7 = models.FloatField(blank=False, default=0.0)


class ResidualValue(models.Model):
    id = models.AutoField(primary_key=True)

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    trim = models.CharField(max_length=100)

    mo_24 = models.FloatField(blank=False, default=0.0)
    mo_27 = models.FloatField(blank=False, default=0.0)
    mo_30 = models.FloatField(blank=False, default=0.0)
    mo_33 = models.FloatField(blank=False, default=0.0)
    mo_36 = models.FloatField(blank=False, default=0.0)
    mo_39 = models.FloatField(blank=False, default=0.0)
    mo_42 = models.FloatField(blank=False, default=0.0)
    mo_45 = models.FloatField(blank=False, default=0.0)
    mo_48 = models.FloatField(blank=False, default=0.0)
    mo_51 = models.FloatField(blank=False, default=0.0)
    mo_54 = models.FloatField(blank=False, default=0.0)
    mo_57 = models.FloatField(blank=False, default=0.0)
    mo_60 = models.FloatField(blank=False, default=0.0)

    mi_10k = models.FloatField(blank=False, default=0.0)
    mi_12k = models.FloatField(blank=False, default=0.0)
    mi_15k = models.FloatField(blank=False, default=0.0)

    multiple_factor = models.IntegerField(blank=False, default=1)
    multiple_mo = models.IntegerField(blank=False, default=24)

