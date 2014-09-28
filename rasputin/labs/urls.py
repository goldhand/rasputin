# urls.py

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^event/load_json/$', 'labs.views.load_json', name='load_json')                                   
)
