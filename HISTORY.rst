.. :changelog:

History
-------

0.2.3 (2016-11-03)
++++++++++++++++++

* Add support for dotted models. Use this feature by defining your Form with a
  field that has a name with double-underscores (e.g. "foo__bar__baz", which
  will become "foo.bar.baz" in the schema's model field).

0.2.2 (2016-11-01)
++++++++++++++++++

* Fix implementation of using initial data in forms. Previously, if you used
  `CharField(initial='foo')` then this information would not be preserved when
  creating the schema.

0.2.1 (2016-10-27)
++++++++++++++++++

* Fix bug in tests so that the tests run successfully in Python 2.7.

0.2.0 (2016-10-25)
++++++++++++++++++

* Add ability to use existing data in form
* DEPRECATED: Any code which previously used `Schema().render(MyForm)` should
  now use `Schema().render(MyForm())` (in other words, `render()` accepts an
  instance of a form, rather than a form itself). To check if you are calling
  the function against contract, you can run your code with `python -Wd`
  (e.g. `python -Wd manage.py runserver`).

0.1.1 (2016-10-18)
++++++++++++++++++

* Add additional tests for schema generation
* Add components for numbers and for selecting between choices
* Add Python 2 support
* Add better documentation
* Fix exception raised on bad widget

0.1.0 (2016-10-11)
++++++++++++++++++

* First release on PyPI.
