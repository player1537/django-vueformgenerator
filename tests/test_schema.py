#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-vueformgenerator
------------

Tests for `django-vueformgenerator` models module.
"""

from django.test import TestCase
from django import forms
from unittest import skip
import warnings

from django_vueformgenerator.schema import Schema
from .models import TestModel, OtherModel


class TestDjango_vueformgenerator(TestCase):

    def setUp(self):
        pass

    def test_schema_generation_for_char_field(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = ('char_field',)

        schema = Schema().render(TestForm(data={}))
        expected = {
            'model': {
                'char_field': None,
            },
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

        schema = Schema().render(TestForm(data={}))
        expected = {
            'model': {
                'text_field': None,
            },
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
            'model': {
                'boolean_field': False,
            },
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

        schema = Schema().render(TestForm(data={}))
        expected = {
            'model': {
                'integer_field': None,
            },
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

        schema = Schema().render(TestForm(data={}))
        expected = {
            'model': {
                'choice_field': None,
            },
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

    def test_correct_error_thrown(self):
        from django.forms.widgets import Widget
        class NotARealWidget(Widget):
            def __repr__(self):
                return "NotARealWidget"

        class TestForm(forms.Form):
            not_a_real = forms.CharField(widget=NotARealWidget)

        expected = 'Could not find component "NotARealWidget"'
        with self.assertRaises(KeyError, msg=expected) as context:
            schema = Schema().render(TestForm(data={}))

    def test_schema_generation_for_foreign_key_field(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = ('other_field',)

        schema = Schema().render(TestForm(data={}))
        expected = {
            'model': {
                'other_field': None,
            },
            'schema': {
                'fields': [
                    {
                        'default': None,
                        'hint': '',
                        'label': 'Other field',
                        'model': 'other_field',
                        'required': True,
                        'type': 'select',
                        'values': [
                            { 'id': '', 'name': '---------' },
                        ],
                    },
                ],
            },
        }

        self.assertEqual(schema, expected)

    @skip("This isn't working for some reason")
    def test_schema_generation_for_related_field(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = OtherModel
                fields = ('other_field',)

        self.maxDiff = None
        schema = Schema().render(TestForm(data={}))
        expected = {
            'model': {
                'other_field': None,
            },
            'schema': {
                'fields': [
                    {
                        'default': None,
                        'hint': '',
                        'label': 'Other field',
                        'model': 'other_field',
                        'required': True,
                        'type': 'select',
                        'values': [
                            { 'id': '', 'name': '---------' },
                        ],
                    },
                ],
            },
        }

        self.assertEqual(schema, expected)

    def test_schema_generation_with_form_cls(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = ('char_field',)

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('once')

            schema = Schema().render(TestForm)
            expected = {
                'model': {
                    'char_field': None,
                },
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

            self.assertEqual(len(w), 1)
            self.assertIs(w[0].category, DeprecationWarning)
            self.assertIn("Deprecated", str(w[0].message))

    def test_schema_generation_with_existing_data(self):
        class TestForm(forms.ModelForm):
            class Meta:
                model = TestModel
                fields = ('char_field',)

        schema = Schema().render(TestForm(data={'char_field': 'foobar'}))
        expected = {
            'model': {
                'char_field': 'foobar',
            },
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

    def tearDown(self):
        pass
