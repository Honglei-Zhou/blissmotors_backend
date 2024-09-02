from django.db import models
from django.contrib.postgres.fields import JSONField
import datetime

class Message(models.Model):
    id = models.AutoField(primary_key=True)

    username = models.CharField(max_length=150, blank=True, null=True)
    session_id = models.UUIDField()
    direction = models.CharField(max_length=20)
    message = JSONField()
    dialogflow_resp = JSONField(blank=True, null=True)

    add_time = models.DateTimeField("Add Time", default=datetime.datetime.now)