from south.modelsinspector import add_introspection_rules
from django.db import models


class OrderedManyToManyField(models.ManyToManyField):

    def contribute_to_class(self, cls, name):
        super(OrderedManyToManyField, self).contribute_to_class(cls, name)

        def get_ordered(attr_name):
            def ordered(model_instance):
                return model_instance._get_ordered_m2m_for(attr_name)
            return ordered

        setattr(cls, name + '_ordered', get_ordered(name))


# Copied the ManyToManyField rules out of South's codebase
add_introspection_rules(
    [
        (
            (OrderedManyToManyField,),
            [],
            {
                "to": ["rel.to", {}],
                "symmetrical": ["rel.symmetrical", {"default": True}],
                "related_name": ["rel.related_name", {"default": None}],
                "db_table": ["db_table", {"default": None}],
                # TODO: Kind of ugly to add this one-time-only option
                "through": ["rel.through", {"ignore_if_auto_through": True}],
            },
        ),
    ],
    [r'^ordered_m2m\.fields\.OrderedManyToManyField']
)