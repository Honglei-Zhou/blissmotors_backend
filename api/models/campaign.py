from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=False)

    date_entered = models.DateTimeField(blank=False, auto_now_add=True)
    date_modified = models.DateTimeField(blank=False, auto_now_add=True)
