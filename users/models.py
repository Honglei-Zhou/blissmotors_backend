from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import datetime
from django.contrib.auth.models import User


def get_permission_code(registration_code):

    options = {
        'BMCM': 600,
        'BMDL': 500,
        'BMEM': 400,
        'BMGM': 300,
        'BMSM': 200,
        'BMAM': 100,
    }

    return options[registration_code[0:4]]


class UserType(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False)

    registration_code = models.CharField(max_length=16, blank=False)

    permission_code = models.IntegerField(blank=False, default=0)

    @classmethod
    def create(cls, user, registration_code):
        if not user or not registration_code:
            return None

        if len(User.objects.all().filter(id=user.id)) != 1:
            return None

        if len(RegistrationCode.objects.all().filter(registration_code=registration_code)) != 1:
            return None

        permission_code = get_permission_code(registration_code)

        user_type = cls(user=user, registration_code=registration_code, permission_code=permission_code)
        return user_type

    def __str__(self):

        return self.permission_code


class PermissionCode(models.Model):

    code = models.IntegerField(blank=False)
    description = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return "Code: %s Description: %s" % (self.code, self.description)


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)

    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    company_name = models.TextField()
    introduction = models.TextField()
    personal_email = models.EmailField()
    office_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)

    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    address_3 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    # subscribe = models.CharField(max_length=5, default='no')

    date_entered = models.DateTimeField(blank=False, auto_now_add=True)
    date_modified = models.DateTimeField(blank=False, auto_now_add=True)


class ContactPerson(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

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
    registration_code = models.CharField(max_length=16, blank=False)
    date_entered = models.DateTimeField(blank=False, auto_now_add=True)
    date_modified = models.DateTimeField(blank=False, auto_now_add=True)


class VerificationCode(models.Model):

    id = models.AutoField(primary_key=True)
    code = models.CharField('Verification Code', max_length=10)
    mobile = models.CharField('Phone', max_length=10)
    add_time = models.DateTimeField('Add Time', default=datetime.datetime.now)

    class Meta:
        verbose_name = "Verification Code"
        verbose_name_plural = verbose_name


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

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

# User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])
