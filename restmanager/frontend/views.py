import requests
import json
from django.shortcuts import render, redirect
import os
import slack
from dotenv import load_dotenv
from django.http import HttpResponse
from . import strings
from django.views.decorators.csrf import csrf_exempt
from fridges.models import Fridge

# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

IP2 = os.getenv('IP2')


@csrf_exempt
def create_fridges(request):
    Fridge.objects.bulk_create([
        Fridge(name="Sauna Fridge", state="Empty", floor="1"),
        Fridge(name="Fridge", state="Full", floor="2"),
        Fridge(name="Fridgey", state="Half-full", floor="3"),
        Fridge(name="Fridgex", state="Half-full", floor="4"),
        Fridge(name="Fridgexy", state="Half-full", floor="5"),
        Fridge(name="Fridgeyx", state="Half-full", floor="6"),
        Fridge(name="Fridgeyxy", state="Half-full", floor="7")
    ])

    return HttpResponse("Created fridges.")


@csrf_exempt
def create_fridges2(request):
    Fridge.objects.bulk_create([
        Fridge(name="Egdirf_01", state="Empty", floor="1"),
        Fridge(name="Egdirf_02", state="Full", floor="2"),
        Fridge(name="Egdirf_03", state="Half-full", floor="3"),
        Fridge(name="Egdirf_04", state="Half-full", floor="4"),
        Fridge(name="Egdirf_05", state="Half-full", floor="5"),
        Fridge(name="Egdirf_06", state="Half-full", floor="6"),
        Fridge(name="Egdirf_07", state="Half-full", floor="7")
    ])

    return HttpResponse("Created fridges 2.")


# Endpoint http://localhost:8069/fridges.
@csrf_exempt
def fridges(request):
    r = requests.get('HTTP://' + IP2 + ':8069/api/fridges/?format=json')
    data = json.loads(r.text)
    data_dict = []
    for item in data:
        dicti = {
            'id': item['id'],
            'name': item['name'],
            'state': item['state'],
            'floor': item['floor'],
        }

        data_dict.append(dicti)
    context = {
        'data': data_dict,
    }
    return render(request, 'frontend/fridges.html', context)


@csrf_exempt
def change_state(request):
    if request.method == 'POST':
        f_name = request.POST.get('name')
        f_id = request.POST.get('id')
        floor_id = request.POST.get('floor')
        username_c = 'Floor: ' + floor_id + ', ' + f_name
        if request.POST.get('state') == 'Empty':
            new_state = 'Full'

        elif request.POST.get('state') == 'Full':
            new_state = 'Half-full'

        else:
            new_state = 'Empty'

        Fridge.objects.filter(id=f_id).update(state=new_state)
        client.chat_postMessage(
            channel=strings.CHANNEL_NAME_1,
            text=f'State: {new_state}',
            username=username_c
        )
    return redirect('/fridges')


def fridge(request):
    r = requests.get('HTTP://' + IP2 + ':8069/api/fridges2/?format=json')
    data = json.loads(r.text)
    data_dict = []
    for item in data:
        dicti = {
            'id': item['id'],
            'name': item['name'],
            'state': item['state'],
            'floor': item['floor'],
        }

        data_dict.append(dicti)
    context = {
        'data': data_dict,
    }
    return render(request, 'frontend/fridge.html', context)

