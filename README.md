# django-model-render
Django models extension that allows define default model templates

## Installation
### Install package from pip

```bash
$ pip install django-model-render
```

### Add app to settings.INSTALLED_APPS
```python
INSTALLED_APPS = (
    ...
    'model_render',
    ...
)
```

If you use jinja, use ```MODEL_RENDER_DEFAULT_EXTENSION``` to configute default template extension.
```
MODEL_RENDER_DEFAULT_EXTENSION = "jinja2"
```
default value is ```html```


### Add mixin to your models
```python
from django.db import models
...
from model_render import ModelRenderMixin

class MyModel(ModelRenderMixin, models.Model):
    # ... fields here

```
## Usage
### Basic usage
Add model template in template folders and see how use it in templates:
```html
    {{ mymodelInstance.render }}
```
### Template search strategy
By default, render method search template in ```$model_app_label$/models/$model_name$.$settings.MODEL_RENDER_DEFAULT_EXTENSION$```

 You can extend this two ways:
#### Use ```Model.template_path``` attr.
Something like
```python
class MyModel(ModelRenderMixin, models.Model):
    template_name="myapp/custom-template.html"
    # ... fields here
```
And all calls ```render()``` method will search in ```"myapp/custom-template.html"```.

#### ```render()``` method argument with argument
Something like

```html
    {{ mymodelInstance.render("myapp/very-custom-template.html") }}
```
Only this call for ```render()``` method will search in ```"myapp/very-custom-template.html"```.

