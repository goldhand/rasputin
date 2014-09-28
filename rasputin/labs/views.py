from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from reports.models import LabReport

@csrf_exempt
def load_json(request):
    if request.is_ajax():
        if request.method == 'POST':
            json_dict = json.loads(request.body)
            for item in json_dict['data']:
                print "data item", item 
    return HttpResponse("OK")
