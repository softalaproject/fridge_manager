import os
import json
import slack
import requests
from dotenv import load_dotenv
from fridges.models import Fridge
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

# Gets slack token from .env file and sets it here
load_dotenv()
slack_client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

# IP2 is the servers IP Address set in .env found in fridge_manager/restmanager
IP2 = os.getenv('IP2', '127.0.0.1')
# D_PORT determines which port the get_request is sent to (the port that the server is running on)
D_PORT = os.getenv('D_PORT', '8100')
# API_URL is here incase versioning happens
API_URL = os.getenv('API_URL', '/api/')
# REQ_URL is where get_request sends its request to
REQ_URL = os.getenv('REQ_URL', f'HTTP://{IP2}:{D_PORT}{API_URL}fridges/?format=json')


def create_json(a_list):
    """ converts given list into json and returns it """
    json_string = json.dumps(a_list)
    return json_string


def create_list(floor, fridge_id, state):
    """ Creates a list and sorts through it depending on what parameters are given in the request that it receives
     Accepts parameters from url id, floor, state and returns a select_list named list """
    select_list = []

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
    r = requests.get(REQ_URL)
    return json.loads(r.text)


@csrf_exempt
def change_state(request):
    """ View for endpoint /api/change_state, which is used to change the state of a fridge and send
    the message to slack """
    # If the requests method which is sent to the endpoint is POST goes into the if logic
    # otherwise redirects back to where the user came from
    if request.method == 'POST':
        fridge_name = request.POST.get('name')
        fridge_id = request.POST.get('id')
        floor_id = request.POST.get('floor')
        channel = request.POST.get('channel')
        username_c = 'Floor: ' + floor_id + ', ' + fridge_name
        new_state = request.POST.get('new_state')

        # updates the fridge objects data in the database with given parameters
        Fridge.objects.filter(id=fridge_id).update(state=new_state)
        slack_client.chat_postMessage(
            channel=f'#{channel}',
            text=f'State: {new_state}',
            username=username_c
        )
    # redirects the requests sender back to where they came from
    # doesnt work if the user has blocked metadata with incognito mode or other means
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@csrf_exempt
def create_fridges(request):
    """ Function only for adding fridges quickly in testing/development """
    fridge_1 = Fridge(name="Sauna FridgeX", state="Empty", floor="1", channel="general")
    fridge_2 = Fridge(name="FridgeX", state="Full", floor="2", channel="general")
    fridge_3 = Fridge(name="FridgeyX", state="Half-full", floor="3", channel="general")
    fridge_4 = Fridge(name="FridgexX", state="Half-full", floor="4", channel="general")
    fridge_5 = Fridge(name="FridgexyX", state="Half-full", floor="5", channel="general")
    fridge_6 = Fridge(name="FridgeyxX", state="Half-full", floor="6", channel="general")
    fridge_7 = Fridge(name="FridgeyxyX", state="Half-full", floor="7", channel="general")

    fridge_1.save()
    fridge_2.save()
    fridge_3.save()
    fridge_4.save()
    fridge_5.save()
    fridge_6.save()
    fridge_7.save()

    return HttpResponse("Created fridges.")
