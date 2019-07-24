from .models import AnyModel
from model_report.report import reports, ReportAdmin

class AnyModelReport(ReportAdmin):
    title = _('AnyModel Report Name')
    model = AnyModel
    fields = [
        'anymodelfield',
    ]
    list_order_by = ('anymodelfield',)
    type = 'report'

reports.register('anymodel-report', AnyModelReport)