from .components import registry
import inspect
import warnings


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

        model = {}
        for schema_field in fields:
            key = schema_field['model']
            initial = form[key].initial
            data = form[key].data

            value = None
            if initial is not None:
                value = initial
            if data is not None:
                value = data

            model[key] = value

        return dict(
            schema=dict(
                fields=fields,
            ),
            model=model,
        )
