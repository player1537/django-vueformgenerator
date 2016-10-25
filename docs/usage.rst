========
Usage
========

To use Django-VueFormGenerator in a project::

    from django_vueformgenerator.schema import Schema
    from django import forms
    import json

    class TestForm(forms.Form):
        title = forms.CharField(max_length=128)
        content = forms.TextField(max_length=1280)

    form = TestForm()  # or TestForm(data={'title': 'My Title'})
    schema = Schema().render(form)
    print(json.dumps(schema))

Then on the frontend, you can use the schema directly::

    <template>
        <vue-form-generator :schema="schema" :model="model"></vue-form-generator>
    </template>

    <script>
    export default {
        // ...
        data() {
            return { /* schema object from Django-VueFormGenerator */ };
        }
        // ...
    }
    </script>

Currently, the fields that are implemented are:

* `django.forms.CharField` which maps to `{ "type": "text" }`

* `django.forms.TextField` which maps to `{ "type": "textArea" }`

* `django.forms.BooleanField` which maps to `{ "type": "checkbox" }`

* `django.forms.IntegerField` which maps to `{ "type": "number" }`

* Any field which uses `django.forms.Field(choices=(...))` which maps to `{ "type": "select" }`

For more information, check:

* `VueFormGenerator's documentation <https://icebob.gitbooks.io/vueformgenerator/content/fields/>`

* `Django Form's documentation <https://docs.djangoproject.com/en/1.10/ref/forms/fields/>`
