import simplejson
from django.db import models


class OrderedM2M(models.Model):
    _ordered_m2m_ordering = models.TextField(blank=True)

    class Meta:
        abstract = True

    def _get_ordered_m2m_for(self, attr_name):
        m2m = getattr(self, attr_name).all()
        order = self._ordered_m2m_ordering
        if m2m.count():
            if order:
                json = simplejson.loads(order)
                attr_ordering = json.get(attr_name, None)
                if attr_ordering:
                    ordered_m2m = []
                    for pk in attr_ordering:
                        ordered_m2m += [obj for obj in m2m if obj.pk == pk]
                    return ordered_m2m + [obj for obj in m2m if obj not in ordered_m2m]
            # For consistency, return it as a list
            return list(m2m)

