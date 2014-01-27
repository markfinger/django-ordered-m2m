from django.contrib.admin.templatetags.admin_static import static
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.safestring import mark_safe
from .settings import WIDGET_STORAGE_ID


class OrderedFilteredSelectMultiple(FilteredSelectMultiple):
    @property
    def media(self):
        media = super(OrderedFilteredSelectMultiple, self).media
        media.add_css({
            'all': [
                static('ordered_m2m/widget.css'),
            ]
        })
        media.add_js([
            static('ordered_m2m/widget.js'),
        ])
        return media

    def render(self, *args, **kwargs):
        output = super(OrderedFilteredSelectMultiple, self).render(*args, **kwargs)

        output += '''
        <script>
            orderedFilteredSelectMultiple = window.orderedFilteredSelectMultiple || {};
            (function(obj) {
                obj.storageID = obj.storageID || '%s';
                obj.targets = obj.targets || [];
                obj.targets.push({
                    id: '%s',
                    field: '%s'
                });
            })(orderedFilteredSelectMultiple);
        </script>
        ''' % (
            # JSON dump element's ID
            WIDGET_STORAGE_ID,
            # Element ID
            kwargs['attrs']['id'] + '_filter',
            # Field name
            kwargs['attrs']['id'].strip('id_'),
        )

        return mark_safe(output)