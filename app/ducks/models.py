# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DuckType(models.Model):
    name = models.CharField(max_length=100)


class Record(models.Model):
    recorddate = models.DateTimeField(default=timezone.now())
    food_type= models.ForeignKey(FoodType, on_delete=models.CASCADE)
    location= models.CharField(max_length=100)
    howmany_ducks = models.PositiveIntegerField()
    duck_type= models.ForeignKey(DuckType, on_delete=models.CASCADE)
    howmuch_food = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.recorddate}'

