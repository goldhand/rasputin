from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from functools import partial
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    r = partial(reverse, request=request, format=format)
    return Response({
        'labreport': {
            'list': r('api:labreport-list'),
            'details': r('api:labreport-detail', args=[1]),

        },})