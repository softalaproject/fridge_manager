import os
import json
import slack
from dotenv import load_dotenv
from fridges.models import Fridge
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect


# Gets slack token from .env file and sets it here
load_dotenv()
slack_client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))


def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]


def create_json(dicti):
    """ converts given dict into json and returns it as a string"""
    json_string = json.dumps(dicti)
    return json_string


def create_json_data_string(floor = None, id = None, state = None):
    """ Accepts parameters if found in url, filters data based on found parameter or returns data which contains all fridge object models values in the database """
    data = Fridge.objects.all().values().order_by('floor')
    # Checks if params exist in request
    if floor is not None:
        data = data.filter(floor=floor)
    elif id is not None:
        data = data.filter(id=id)
    elif state is not None:
        state = state.capitalize()
        data = data.filter(state=state).order_by('floor')
    data_dict = ValuesQuerySetToDict(data)
    data_json = json.dumps(data_dict)
    return json.loads(data_json)


def create_uniq_floors(request):
    """ queryset with distinct floors """
    floors = Fridge.objects.all().values_list('floor', flat=True).distinct().order_by('floor')
    data_dict = ValuesQuerySetToDict(floors)
    floors_json = json.dumps(data_dict)
    return json.loads(floors_json)


def create_floor_list(request):
    """ Creates a list of unique floors found in fridges table in the database and returns it """
    floor_list = []
    # adds unique floor numbers found in the create_uniq_floors(request)
    for item in create_uniq_floors(request):
        if item not in floor_list:
            floor_list.append(item)
    return floor_list


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
