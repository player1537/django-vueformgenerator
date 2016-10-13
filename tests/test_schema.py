#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-vueformgenerator
------------

Tests for `django-vueformgenerator` models module.
"""

from django.test import TestCase
from django import forms

from django_vueformgenerator.schema import Schema
from .models import TestModel


class TestDjango_vueformgenerator(TestCase):

    def setUp(self):
        pass

    def test_schema_generation_for_char_field(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = ('char_field',)

        schema = Schema().render(TestForm)
        expected = {
            'schema': {
                'fields': [
                    {
                        'default': None,
                        'hint': '',
                        'label': 'Char field',
                        'model': 'char_field',
                        'required': True,
                        'type': 'text'
                    },
                ],
            },
        }

        self.assertEqual(schema, expected)

    def test_schema_generation_for_text_field(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = ('text_field',)

        schema = Schema().render(TestForm)
        expected = {
            'schema': {
                'fields': [
                    {
                        'default': None,
                        'hint': '',
                        'label': 'Text field',
                        'model': 'text_field',
                        'required': True,
                        'rows': 10,
                        'type': 'textArea'
                    },
                ],
            },
        }

        self.assertEqual(schema, expected)

    def test_schema_generation_for_boolean(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = ('boolean_field',)

        schema = Schema().render(TestForm)
        expected = {
            'schema': {
                'fields': [
                    {
                        'default': None,
                        'hint': '',
                        'label': 'Boolean field',
                        'model': 'boolean_field',
                        'required': False,
                        'type': 'checkbox'
                    }
                ],
            },
        }

        self.assertEqual(schema, expected)

    def test_schema_generation_for_integer(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = ('integer_field',)

        schema = Schema().render(TestForm)
        expected = {
            'schema': {
                'fields': [
                    {
                        'default': None,
                        'hint': '',
                        'label': 'Integer field',
                        'model': 'integer_field',
                        'required': True,
                        'type': 'number',
                    }
                ],
            },
        }

        self.assertEqual(schema, expected)

    def test_schema_generation_for_choice(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = ('choice_field',)

        schema = Schema().render(TestForm)
        expected = {
            'schema': {
                'fields': [
                    {
                        'default': None,
                        'hint': '',
                        'label': 'Choice field',
                        'model': 'choice_field',
                        'required': True,
                        'type': 'select',
                        'values': [
                            { 'id': '', 'name': '---------' },
                            { 'id': 'FR', 'name': 'Freshman' },
                            { 'id': 'SO', 'name': 'Sophomore' },
                            { 'id': 'JR', 'name': 'Junior' },
                            { 'id': 'SR', 'name': 'Senior' },
                        ],
                    }
                ],
            },
        }

        self.assertEqual(schema, expected)

    def tearDown(self):
        pass
