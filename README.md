django-ordered-m2m
==================

Adds ordering to the Admin's widget for Many-To-Many.

![Widget example](https://raw.github.com/markfinger/django-ordered-m2m/master/widget-example.png)


Install
-------
`pip install django-ordered-m2m`


Example
-------
```python

# models.py
from ordered_m2m.fields import OrderedManyToManyField
from ordered_m2m.models import OrderedM2M

class Article(OrderedM2M):
    categories = OrderedManyToManyField('categories.Category')


# admin.py
from ordered_m2m.admin import OrderedM2MAdmin
from .models import Article

class ArticleAdmin(OrderedM2MAdmin):
    pass

admin.site.register(Article, ArticleAdmin)


# Template

{% for category in article.categories_ordered %}
    {{ category }}
{% endfor %}
```

`ordered_m2m.fields.OrderedManyToManyField`
-------------------------------------------
Dynamically contributes a extra method to the parent class which allows you to receive the relations 
in the order specified by the admin's widget.

For example: if your field was named `categories`, the ordered set of relations will be named
`categories_ordered`.

`*_ordered` returns the relations in a standard Python List.

Inherits from `django.db.models.ManyToManyField`.


`ordered_m2m.models.OrderedM2M`
-------------------------------
Provides an extra TextField, `_ordered_m2m_ordering`, which is used by each of the widgets to store their ordering.

Inherits from `django.db.models.Model`.


`ordered_m2m.admin.OrderedM2MAdmin`
-----------------------------------
Handles the legwork of setting up the widgets.

Inherits from `django.contrib.admin.ModelAdmin`.
