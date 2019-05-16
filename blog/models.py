# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class DataItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    lastprice = models.CharField(max_length=100, default='')
    sinceclose = models.CharField(max_length=100, default='')
    sinceopen = models.CharField(max_length=100, default='')
    isin = models.CharField(max_length=100, default='')
    place = models.CharField(max_length=100, default='')