from django.contrib import admin
from ordered_m2m.fields import OrderedManyToManyField
from ordered_m2m.widgets import OrderedFilteredSelectMultiple


class OrderedM2MAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if isinstance(db_field, OrderedManyToManyField):
            return self.formfield_for_ordered_manytomany(db_field, **kwargs)
        else:
            return super(OrderedM2MAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def formfield_for_ordered_manytomany(self, db_field, **kwargs):
        kwargs['widget'] = OrderedFilteredSelectMultiple(
            db_field.verbose_name,
            (db_field.name in self.filter_vertical)
        )
        del kwargs['request']
        return db_field.formfield(**kwargs)