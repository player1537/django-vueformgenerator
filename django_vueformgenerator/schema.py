from .components import registry
import inspect
import warnings
from collections import defaultdict


def tree():
    return defaultdict(tree)

def tree_to_regular(d):
    if isinstance(d, defaultdict):
        d = {k: tree_to_regular(v) for k, v in d.items()}
    return d

class Schema(object):
    """
    A schema takes in a form and returns a dictionary representing the fields
    in it.
    """
    def render(self, form):
        if inspect.isclass(form):
            warnings.warn(
                "Deprecated: Schema().render() accepts a form now, not a form class.",
                DeprecationWarning,
            )

            form = form(data={})

        for (name, field) in form.fields.items():
            field.__name__ = name

        fields = []
        for field in form.fields.values():
            component = registry.lookup(field)
            fields.append(component.render(field))

        model = tree()
        for schema_field in fields:
            key = schema_field['model'].replace('.', '__')
            initial = form[key].initial
            data = form[key].data

            value = None
            if initial is not None:
                value = initial
            if data is not None:
                value = data

            m = prev = model
            for k in schema_field['model'].split('.'):
                prev = m
                m = m[k]

            prev[k] = value

        model = tree_to_regular(model)

        return dict(
            schema=dict(
                fields=fields,
            ),
            model=model,
        )
