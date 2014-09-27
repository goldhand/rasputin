from tastypie.resources import ModelResource
from models import LabReport


class LabReportResource(ModelResource):
    class Meta:
        queryset = LabReport.objects.all()
        resource_name = 'labreport'
