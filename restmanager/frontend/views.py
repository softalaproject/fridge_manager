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
from django.core import serializers 

# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

IP2 = os.getenv('IP2')


# Endpoint http://localhost:8069/items.
@csrf_exempt
def fridges(request):
    r = requests.get('HTTP://' + IP2 + ':8069/api/fridges/?format=json')
    data = json.loads(r.text)
    # print(r.text)
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
    # print(data_dict)
    return render(request, 'frontend/fridges.html', context)
    # t = requests.get('https://sauna.eficode.fi/get-latest')
    # temp_data = json.loads(t.text)
    # t_dict = []
    # temp = round(temp_data['temperature'], 1)
    # humid = round(temp_data['humidity'], 1)
    # temps = {
    #     'temp': temp,
    #     'humid': humid
    # }
    # t_dict.append(temps)
#     { %
#     for t in temp %}
#     < nav
#     id = "navbarr"
#
#     class ="navbar navbar-light bg-light" >
#
#     < span
#
#     class ="navbar-text" > < / span >
#
#     < span
#
#     class ="navbar-text" > {{t.temp}} °C | | {{t.humid}} % < / span >
#
#     < span
#     id = "time"
#
#     class ="navbar-text" > < / span >
#
# < / nav >
# { % endfor %}


@csrf_exempt
def change_state(request):
    if request.method == 'POST':
        f_name = request.POST.get('name')
        f_id = request.POST.get('id')
        floor_id = request.POST.get('floor')
        if request.POST.get('state') == 'Empty':
            new_state = 'Full'

        elif request.POST.get('state') == 'Full':
            new_state = 'Half-full'

        else:
            new_state = 'Empty'

        Fridge.objects.filter(id=f_id).update(state=new_state)
        client.chat_postMessage(
            channel=strings.CHANNEL_NAME_1,
            text=f'Fridge with name: {f_name} and ID: {f_id} from floor no: {floor_id} had its state set to: {new_state}.'
        )
    return redirect('/fridges')


def fridge(request):
    data = serializers.serialize("python", Fridge.objects.all().filter(floor=1))
    print(data)
    all_entries = Fridge.objects.all().filter(floor=1)
    print(all_entries)
    one_entry = Fridge.objects.get(id=1)
    print(one_entry)
    return render(request, 'frontend/fridge.html')


@csrf_exempt
def post_beer(request):
    if request.method == "POST":
        client.chat_postMessage(
            channel=strings.CHANNEL_NAME_1,
            text=strings.SLACK_MESSAGE_2
        )
    return HttpResponse("ok")


@csrf_exempt
def post_no_beer(request):
    if request.method == "POST":
        client.chat_postMessage(
            channel=strings.CHANNEL_NAME_1,
            text=strings.SLACK_MESSAGE_1
        )
    return HttpResponse("ok")
