from django.db import models
import datetime

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    modified = models.DateTimeField(auto_now=True, default=datetime.datetime.now())


    class Meta:
        abstract = True
