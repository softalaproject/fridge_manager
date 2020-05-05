from django.shortcuts import render
from django.http import HttpResponse
from . import urlfunctions


def fridges(request):
    """ View for /fridges/ endpoint, uses create_list() passing the received request to it and then passing the filtered
    list as context to the template fridges.html """
    floor = request.GET.get('floor')
    fridge_id = request.GET.get('id')
    state = request.GET.get('state')

    context = {
        'data': urlfunctions.create_list(floor, fridge_id, state),
    }
    return render(request, 'frontend/fridges.html', context)


def json_view(request):
    """ view found at /api/json/ uses the create_list function, meaning it can use all the parameters listed in
    the function """
    filtered_list = urlfunctions.create_list(request)
    json_response = urlfunctions.create_json(filtered_list)
    return HttpResponse(json_response)


def floors(request):
    """ View for index and /floors/ endpoint, passes create_floor_list() which creates a list of unique floors
     and passes it as context to template floors.html """
    context = {
        'data': urlfunctions.create_floor_list(),
    }
    return render(request, 'frontend/floors.html', context)



