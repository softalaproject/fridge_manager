import os
import json
import slack
import requests
from . import channels
from dotenv import load_dotenv
from fridges.models import Fridge
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

IP2 = os.getenv('IP2')
D_PORT = "8080"

# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))


@csrf_exempt
def get_request():
    r = requests.get('HTTP://' + IP2 + ':' + D_PORT + '/api/fridges/?format=json')
    return json.loads(r.text)


# Endpoint http://localhost:PORTNO/fridges.
@csrf_exempt
def fridges(request):
    data = get_request()
    data_list = []
    select_list = []
    floor = request.GET.get('floor')
    fridge_id = request.GET.get('id')
    state = request.GET.get('state')

    for item in data:
        data_dict = {
            'id': item['id'],
            'name': item['name'],
            'state': item['state'],
            'floor': item['floor'],
        }
        data_list.append(data_dict)

    if floor is not None:
        int_floor = int(floor)
        for item in data_list:
            if item['floor'] == int_floor:
                select_list.append(item)
    elif fridge_id is not None:
        int_fridge_id = int(fridge_id)
        for item in data_list:
            if item['id'] == int_fridge_id:
                select_list.append(item)
    elif state is not None:
        for item in data_list:
            if item['state'] == state:
                select_list.append(item)
    else:
        for item in data_list:
            select_list.append(item)

    context = {
        'data': select_list,
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


