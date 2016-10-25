=============================
Django-VueFormGenerator
=============================

.. image:: https://badge.fury.io/py/django-vueformgenerator.png
    :target: https://badge.fury.io/py/django-vueformgenerator

.. image:: https://travis-ci.org/player1537/django-vueformgenerator.png?branch=master
    :target: https://travis-ci.org/player1537/django-vueformgenerator

A package to help bridge the gap between Django's Forms and VueFormGenerator's Schemas using DjangoRestFramework.

Documentation
-------------

The full documentation is at https://django-vueformgenerator.readthedocs.org.

Quickstart
----------

Install Django-VueFormGenerator::

    pip install django-vueformgenerator

Then use it in a project::

    from django_vueformgenerator.schema import Schema
    from django import forms
    import json

    class TestForm(forms.Form):
        title = forms.CharField(max_length=128)
        content = forms.TextField(max_length=1280)

    form = TestForm()  # or TestForm(data={'title':'My Title'})
    schema = Schema().render(form)
    print(json.dumps(schema))


Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
