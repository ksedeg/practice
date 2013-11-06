from django.db import models
from django.contrib import admin
from library.models import Book
from utils.models import TimeStampedModel

import datetime
# Create your models here.


class Customer(TimeStampedModel):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.TextField()
    is_approved = models.BooleanField()
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Order(TimeStampedModel):
    itemId = models.ForeignKey(Book)
    created_date = models.DateField(default=datetime.datetime.now())
    customer = models.ForeignKey(Customer, default=0)

    def __unicode__(self):
        return self.itemId
