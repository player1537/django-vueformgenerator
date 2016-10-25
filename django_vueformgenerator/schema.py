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

        fields = [
            registry.lookup(field).render(field)
            for field in form.fields.values()
        ]

        model = {
            schema_field['model']: form[schema_field['model']].data
            for schema_field in fields
        }

        return dict(
            schema=dict(
                fields=fields,
            ),
            model=model,
        )
