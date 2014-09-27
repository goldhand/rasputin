from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from reports.models import LabReport
from .lab_serializers import LabReportSerializer
from labs.models import Lab

def get_lab_from_request(request):
    '''
    returns the lab from request.origin
    '''
    return Lab.objects.get_or_create(id=1)[0]


class LabReportViewSet(ModelViewSet):
    '''
    Lab reports list and create
    '''
    model = LabReport
    serializer_class = LabReportSerializer

    
    def pre_save(self, obj):
        # associate lab from request
        obj.lab = get_lab_from_request(self.request)
        super(LabReportViewSet, self).pre_save(obj)

    def post_save(self, obj, created=True):
        # send to third party apis
        super(LabReportViewSet, self).post_save(obj, created=created)