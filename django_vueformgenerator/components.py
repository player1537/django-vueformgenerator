from django.forms import widgets
from .fields import (
    Field, Attr, Name, Literal, Func,
)
from collections import OrderedDict
import six


class ComponentRegistry(object):
    def __init__(self):
        self.components = dict()

    def add(self, widget_cls, component_cls):
        self.components[widget_cls] = component_cls()

    def lookup(self, field):
        for (widget_cls, component) in self.components.items():
            if isinstance(field.widget, widget_cls):
                return component
        raise KeyError('Could not find component "{!r}"'.format(component))


registry = ComponentRegistry()


def register_schema_for(widget_cls, registry=registry):
    def wrapper(component_cls):
        registry.add(widget_cls, component_cls)
        return component_cls
    return wrapper


class DeclarativeFieldsMetaclass(type):
    """
    Metaclass that collects Fields declared on the base classes.
    """
    def __new__(mcs, name, bases, attrs):
        current_fields = []
        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                current_fields.append((key, value))
                attrs.pop(key)

        attrs['declared_fields'] = OrderedDict(current_fields)

        new_class = super(DeclarativeFieldsMetaclass, mcs).__new__(
            mcs, name, bases, attrs
        )

        # Walk through the MRO.
        declared_fields = OrderedDict()
        for base in reversed(new_class.__mro__):
            # Collect fields from base class.
            if hasattr(base, 'declared_fields'):
                declared_fields.update(base.declared_fields)

            # Field shadowing.
            for attr, value in base.__dict__.items():
                if value is None and attr in declared_fields:
                    declared_fields.pop(attr)

        new_class.base_fields = declared_fields
        new_class.declared_fields = declared_fields
        new_class.attrs = declared_fields

        return new_class


class Component(object):
    def __init__(self, attrs=None):
        if attrs is None and self.attrs is None:
            self.attrs = dict()
        elif attrs is not None and self.attrs is not None:
            self.attrs.update(attrs)
        else:
            pass  # Don't need to do anything

    def render(self, field, attrs=None):
        if attrs is None:
            attrs = dict()

        d = dict()

        for (key, value) in self.attrs.items():
            d[key] = value.render(field=field)

        for (key, value) in attrs:
            d[key] = value.render(field=field)

        return d


class BaseComponent(six.with_metaclass(DeclarativeFieldsMetaclass, Component)):
    label = Attr('label')
    hint = Attr('help_text')
    model = Name()
    default = Attr('default', default=None)
    required = Attr('required')


@register_schema_for(widgets.TextInput)
class TextComponent(six.with_metaclass(DeclarativeFieldsMetaclass, BaseComponent)):
    type = Literal('text')


@register_schema_for(widgets.Textarea)
class TextAreaComponent(six.with_metaclass(DeclarativeFieldsMetaclass, BaseComponent)):
    type = Literal('textArea')
    rows = Func(lambda field: int(field.widget.attrs['rows']))


@register_schema_for(widgets.CheckboxInput)
class CheckboxComponent(six.with_metaclass(DeclarativeFieldsMetaclass, BaseComponent)):
    type = Literal('checkbox')
