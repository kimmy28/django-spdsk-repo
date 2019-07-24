import django_tables2 as tables
from django_tables2 import Table, TableBase
from .models import InputBS, InputOP


class BaseTable(Table):
    def __init__(self, *args, **kwargs):
        super(BaseTable, self).__init__(*args, **kwargs)

class opdataTable(tables.Table):
    change = tables.TemplateColumn('''<a href="/schedule/update_schedule/{{ record.id }}">Update</a> / Cancel / Event /
                                        <a href="/schedule/delete_schedule/{{ record.id }}"
                                        onclick="return confirm('Are you sure you want to delete this?')">Delete</a>''', verbose_name=u'Change', )
    class Meta:
        model = InputOP
        template_name = 'django_tables2/bootstrap-responsive.html'
        row_attrs = {
            'data-id': lambda record: record.pk
        }

class bsdataTable(tables.Table):
    change = tables.TemplateColumn('''<a href="/schedule/update_schedule/{{ record.id }}">Update</a> / Cancel / Event /
                                        <a href="/schedule/delete_schedule/{{ record.id }}"
                                        onclick="return confirm('Are you sure you want to delete this?')">Delete</a>''', verbose_name=u'Change', )

    class Meta:
        model = InputBS
        template_name = 'django_tables2/bootstrap-responsive.html'

class UselessMixin(object):
    extra = tables.Column()

class ReportTable(tables.Table):
    template_name = 'django_tables2/bootstrap-responsive.html'