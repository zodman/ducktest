# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Record, DuckType, FoodType


admin.site.register(Record)
admin.site.register(DuckType)
admin.site.register(FoodType)
