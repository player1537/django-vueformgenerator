from .components import registry

class Schema(object):
    """
    A schema takes in a form and returns a dictionary representing the fields
    in it.
    """
    def render(self, form_cls):
        return dict(
            schema=dict(
                fields=[
                    registry.lookup(field).render(field)
                    for (name, field) in form_cls().fields.items()
                ],
            ),
        )
