from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CarMake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    source_url = models.TextField(blank=True, default='')
    description = models.CharField(max_length=255)

    logo = models.TextField(blank=True, default='')

    class Meta:
        managed = False
        db_table = 'car_make'

    def __str__(self):
        return self.name


class CarModel(models.Model):
    id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    description = models.CharField(max_length=255)
    referer = models.TextField(blank=True, default='')

    logo = models.TextField(blank=True, default='')

    class Meta:
        managed = False
        db_table = 'car_model'

    def __str__(self):
        return _('%s %s') % (self.make, self.name)


class CarType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    logo = models.TextField(blank=True, default='')

    class Meta:
        managed = False
        db_table = 'car_type'

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

    class Meta:
        managed = False
        db_table = 'car_trim'

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

    class Meta:
        managed = False
        db_table = 'car_specs'

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

    class Meta:
        managed = False
        db_table = 'car_image'


class CarImagePath(models.Model):
    id = models.AutoField(primary_key=True)

    path_key = models.TextField()
    path_dest = models.TextField()

    class Meta:
        managed = False
        db_table = 'car_image_path'


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

    class Meta:
        managed = False
        db_table = 'car'

    def __str__(self):
        return _("%s %s %s %s") % (self.year, self.make, self.model, self.trim)

