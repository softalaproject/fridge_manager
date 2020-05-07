from django.shortcuts import render
from django.http import HttpResponse
from . import urlfunctions
from fridges.models import Fridge
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


def fridges(request):
    """ View for /fridges/ endpoint, uses create_list() passing the received request to it and then passing the filtered
    list as context to the template fridges.html """
    floor = request.GET.get('floor')
    id = request.GET.get('id')

    context = {
        'data': urlfunctions.create_json_data_string(floor, id),
    }
    return render(request, 'frontend/fridges.html', context)


def json_view(request):
    """ view found at /api/json/ uses the create_list function, meaning it can use all the parameters listed in
    the function  """
    floor = request.GET.get('floor')
    fridge_id = request.GET.get('id')
    state = request.GET.get('state')

    filtered_string = urlfunctions.create_json_data_string(floor, fridge_id)
    json_response = urlfunctions.create_json(filtered_string)
    return HttpResponse(json_response)


def floors(request):
    """ View for index and /floors/ endpoint, passes create_floor_list() which creates a list of unique floors
     and passes it as context to template floors.html """
    context = {
        'data': urlfunctions.create_floor_list(request),
    }
    return render(request, 'frontend/floors.html', context)



