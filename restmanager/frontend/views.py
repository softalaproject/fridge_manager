import os
import json
import slack
import requests
from dotenv import load_dotenv
from fridges.models import Fridge
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

# Gets slack token from .env file and sets it here
load_dotenv()
slack_client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

# IP2 is the servers IP Address set in .env found in fridge_manager/restmanager
IP2 = os.getenv('IP2', "127.0.0.1")
# D_PORT is set only here, determines which port the get_request is sent to (the port that the server is running on)

D_PORT = os.getenv('D_PORT', "8100")


def create_floor_list():
    """ Creates a list of unique floors found in fridges table in the database and returns it """
    floor_list = []

    # adds unique floor numbers found in the get_request()
    for item in get_request():
        if item['floor'] not in floor_list:
            floor_list.append(item['floor'])
    return sorted(floor_list)


def get_request():
    """ Sends get request to api endpoint /api/fridges/ which returns a json object with all the fridges in
    the database """
    r = requests.get('HTTP://' + IP2 + ':' + D_PORT + '/api/fridges/?format=json')
    return json.loads(r.text)


def create_list(request):
    """ Creates a list and sorts through it depending on what parameters are given in the request that it receives
     Accepts parameters from url id, floor, state and returns a select_list named list """
    select_list = []
    floor = request.GET.get('floor')
    fridge_id = request.GET.get('id')
    state = request.GET.get('state')

    # loops through data from get_request()
    for item in get_request():
        # if the request has a given parameter floor it is added to select_list
        if floor is not None:
            int_floor = int(floor)
            if item['floor'] == int_floor:
                select_list.append(item)
        elif fridge_id is not None:
            int_fridge_id = int(fridge_id)
            if item['id'] == int_fridge_id:
                select_list.append(item)
        elif state is not None:
            if item['state'].lower() == state.lower():
                select_list.append(item)
        # if the request has no given parameters, adds all data from get_request() to select_list
        else:
            select_list.append(item)
    return select_list


def create_json(a_list):
    """ converts given list into json and returns it """
    json_string = json.dumps(a_list)
    return json_string


def json_view(request):
    """ view found at /api/json/ uses the create_list function, meaning it can use all the parameters listed in
    the function """
    filtered_list = create_list(request)
    json_response = create_json(filtered_list)
    return HttpResponse(json_response)


def floors(request):
    """ View for index and /floors/ endpoint, passes create_floor_list() which creates a list of unique floors
     and passes it as context to template floors.html """
    context = {
        'data': create_floor_list(),
    }
    return render(request, 'frontend/floors.html', context)


def fridges(request):
    """ View for /fridges/ endpoint, uses create_list() passing the received request to it and then passing the filtered
    list as context to the template fridges.html """
    context = {
        'data': create_list(request),
    }

    return render(request, 'frontend/fridges.html', context)


def change_state(request):
    """ View for endpoint /api/change_state, which is used to change the state of a fridge and send
    the message to slack """
    # If the requests method which is sent to the endpoint is POST goes into the if logic
    # otherwise redirects back to where the user came from
    if request.method == 'POST':
        fridge_name = request.POST.get('name')
        fridge_id = request.POST.get('id')
        floor_id = request.POST.get('floor')
        channel_msg = request.POST.get('channel_msg')
        username_c = 'Floor: ' + floor_id + ', ' + fridge_name

        if request.POST.get('state') == 'Empty':
            new_state = 'Full'
        elif request.POST.get('state') == 'Full':
            new_state = 'Half-full'
        else:
            new_state = 'Empty'

        # updates the fridge objects data in the database with given parameters
        Fridge.objects.filter(id=fridge_id).update(state=new_state)
        slack_client.chat_postMessage(
            channel=f'#{channel_msg}',
            text=f'State: {new_state}',
            username=username_c
        )
    # redirects the requests sender back to where they came from
    # doesnt work if the user has blocked metadata with incognito mode or other means
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

