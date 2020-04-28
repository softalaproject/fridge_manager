import os
import json
import slack
import requests
from . import channels
from dotenv import load_dotenv
from fridges.models import Fridge
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

IP2 = os.getenv('IP2')
D_PORT = "8100"


@csrf_exempt
def get_request():
    r = requests.get('HTTP://' + IP2 + ':' + D_PORT + '/api/fridges/?format=json')
    return json.loads(r.text)


def create_list(request):
    select_list = []
    floor = request.GET.get('floor')
    fridge_id = request.GET.get('id')
    state = request.GET.get('state')

    for item in get_request():
        if floor is not None:
            int_floor = int(floor)
            if item['floor'] == int_floor:
                select_list.append(item)
        elif fridge_id is not None:
            int_fridge_id = int(fridge_id)
            if item['id'] == int_fridge_id:
                select_list.append(item)
        elif state is not None:
            if item['state'] == state:
                select_list.append(item)
        else:
            select_list.append(item)
    return select_list


def create_json(a_list):
    my_json_string = json.dumps(a_list)
    return my_json_string


def json_view(request):
    filtered_list = create_list(request)
    a = create_json(filtered_list)
    return HttpResponse(a)


# Endpoint http://localhost:PORTNO/fridges.
@csrf_exempt
def fridges(request):
    context = {
        'data': create_list(request),
    }

    return render(request, 'frontend/fridges.html', context)


@csrf_exempt
def change_state(request):
    if request.method == 'POST':
        fridge_name = request.POST.get('name')
        fridge_id = request.POST.get('id')
        floor_id = request.POST.get('floor')
        username_c = 'Floor: ' + floor_id + ', ' + fridge_name

        if request.POST.get('state') == 'Empty':
            new_state = 'Full'
        elif request.POST.get('state') == 'Full':
            new_state = 'Half-full'
        else:
            new_state = 'Empty'

        Fridge.objects.filter(id=fridge_id).update(state=new_state)
        client.chat_postMessage(
            channel=channels.CHANNEL_NAME_1,
            text=f'State: {new_state}',
            username=username_c
        )
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

