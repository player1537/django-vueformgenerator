#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-vueformgenerator
------------

Tests for `django-vueformgenerator` models module.
"""

from django.db import models


class TestModel(models.Model):
    char_field = models.CharField(max_length=128)
    text_field = models.TextField(max_length=1024)
    boolean_field = models.BooleanField(default=False)
    integer_field = models.IntegerField()
    choice_field = models.CharField(max_length=2, choices=(
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
    ))
    other_field = models.OneToOneField('OtherModel', related_name='other_field')

class OtherModel(models.Model):
    char_field = models.CharField(max_length=16)
