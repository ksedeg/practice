# -*- coding: utf-8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from django.contrib import admin
from orders.models import *
from library.models import *

admin.site.register(Order)
admin.site.register(Customer)
