
try:
    from django.conf.urls import *
except ImportError:  # django < 1.4
    from django.conf.urls.defaults import *

from api.lab_views import LabReportViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'lab_reports', LabReportViewSet)


urlpatterns = router.urls + patterns('api.views',
                       url(r'^$', 'api_root', name="root"),
                       )