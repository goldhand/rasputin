# urls.py

from django.conf.urls import patterns, include, url
from api import LabReportResource

entry_resource = LabReportResource()

urlpatterns = patterns('',
    # example /dal/api/labreport/?format=json
    (r'^api/', include(entry_resource.urls)),
)
