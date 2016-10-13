from .components import registry


class Schema(object):
    """
    A schema takes in a form and returns a dictionary representing the fields
    in it.
    """
    def render(self, form_cls):
        fields = form_cls().fields

        for (name, field) in fields.items():
            field.__name__ = name

        return dict(
            schema=dict(
                fields=[
                    registry.lookup(field).render(field)
                    for field in fields.values()
                ],
            ),
        )
