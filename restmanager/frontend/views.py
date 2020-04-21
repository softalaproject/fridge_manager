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


def create_fridges(request):
    fridge_1 = Fridge(name="Sauna Fridge", state="Empty", floor="1")
    fridge_2 = Fridge(name="fridge", state="Full", floor="2")
    fridge_3 = Fridge(name="fridgey", state="Half-full", floor="3")
    fridge_4 = Fridge(name="fridgex", state="Half-full", floor="4")
    fridge_5 = Fridge(name="fridgexy", state="Half-full", floor="5")
    fridge_6 = Fridge(name="fridgeyx", state="Half-full", floor="6")
    fridge_7 = Fridge(name="fridgeyxy", state="Half-full", floor="7")

    fridge_1.save()
    fridge_2.save()
    fridge_3.save()
    fridge_4.save()
    fridge_5.save()
    fridge_6.save()
    fridge_7.save()

    return HttpResponse("Created fridges")


# Endpoint http://localhost:8069/items.
@csrf_exempt
def items(request):
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

    r = requests.get('HTTP://' + IP2 + ':8069/api/items/?format=json')
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
    return render(request, 'frontend/items.html', context)


@csrf_exempt
def change_item(request):
    # print(request.POST)
    if request.method == 'POST':
        # url = 'http://' + IP2 + ':8069/api/items/1/?format=json'
        # r = requests.get(url)
        f_name = request.POST.get('name')
        f_id = request.POST.get('id')
        if request.POST.get('state') == 'Empty':
            new_state = 'Full'

        elif request.POST.get('state') == 'Full':
            new_state = 'Half'

        else:
            new_state = 'Empty'

        Fridge.objects.filter(id=f_id).update(state=new_state)
        client.chat_postMessage(
            channel=strings.CHANNEL_NAME_1,
            text=f'Fridge ID:{f_id} and Name: {f_name} state set to: {new_state}'
        )
    return redirect('/items')


def fridge(request):
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
