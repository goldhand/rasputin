from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from reports.models import LabReport



class LabReportViewSet(ModelViewSet):
    model = LabReport
