class Field(object):
    def render(self, field):
        raise NotImplementedError('Field.render needs to be defined')


class Attr(Field):
    def __init__(self, attr, default=None, type=None):
        self.attr = attr
        self.default = default
        if type is None:
            self.type = lambda x: x
        else:
            self.type = type

    def render(self, field):
        try:
            x = field
            for attr in self.attr.split('.'):
                x = getattr(x, attr)
            return self.type(x)
        except AttributeError:
            return self.default


class Name(Field):
    def render(self, field):
        return field.__name__


class Func(Field):
    def __init__(self, func):
        self.func = func

    def render(self, field):
        return self.func(field)


class Literal(Field):
    def __init__(self, value):
        self.value = value

    def render(self, *args, **kwargs):
        return self.value
