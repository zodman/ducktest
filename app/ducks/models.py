# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django.utils.timezone
from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        ordering = ("name",)
        get_latest_by = "id"

    def __str__(self):
        return self.name

class DuckType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name", )
        get_latest_by = "id"


    def __str__(self):
        return self.name


class Record(models.Model):
    recorddate = models.DateTimeField(default=django.utils.timezone.now,
                                      help_text="YYYY-mm-dd HH:MM:SS")
    food_type= models.ForeignKey(FoodType, on_delete=models.CASCADE)
    location= models.CharField(max_length=100)
    howmany_ducks = models.PositiveIntegerField()
    duck_type= models.ForeignKey(DuckType, on_delete=models.CASCADE)
    howmuch_food = models.CharField(max_length=100)

    class Meta:
        ordering = ("recorddate",)
        get_latest_by = "id"

    def __str__(self):
        return f'{self.recorddate}'

