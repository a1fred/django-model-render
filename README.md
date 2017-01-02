[![Build Status](https://travis-ci.org/a1fred/django-model-render.svg?branch=master)](https://travis-ci.org/a1fred/django-model-render)
[![Coverage Status](https://coveralls.io/repos/github/a1fred/django-model-render/badge.svg?branch=master)](https://coveralls.io/github/a1fred/django-model-render?branch=master)
[![PyPI version](https://badge.fury.io/py/django-model-render.svg)](https://badge.fury.io/py/django-model-render)

Django models extension that allows define model templates

# Installation
## Install package from pip

```bash
$ pip install django-model-render
```

## Add app to settings.INSTALLED_APPS
```python
INSTALLED_APPS = (
    ...
    'model_render',
    ...
)
```

If you use jinja, use ```MODEL_RENDER_DEFAULT_EXTENSION``` to configute default template extension.
```python
MODEL_RENDER_DEFAULT_EXTENSION = "jinja2"
```
default value is ```html```


## Add mixin to your models
```python
from django.db import models
...
from model_render import ModelRenderMixin

class MyModel(ModelRenderMixin, models.Model):
    # ... fields here

```
# Usage
## Basic usage
Add model template in template folders and see how use it in templates:
```html
    {{ mymodelInstance.render }}
```
## Template search strategy
### By default
```render()``` method search template in ```<app_label>/models/<model_name>.<settings.MODEL_RENDER_DEFAULT_EXTENSION>```

 You can extend this two ways:
### Use ```Model.template_path``` attr.
Something like
```python
class MyModel(ModelRenderMixin, models.Model):
    template_name="myapp/custom-template.html"
    # ... fields here
```
And all calls ```render()``` method will search in ```"myapp/custom-template.html"```.

### ```render()``` method argument with argument
Something like

```html
    {{ mymodelInstance.render("myapp/very-custom-template.html") }}
```
Only this call for ```render()``` method will search in ```"myapp/very-custom-template.html"```.

```render(template=..., additional={'myvar': 123})``` adds myvar to in-template vars.
