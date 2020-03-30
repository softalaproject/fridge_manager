import requests
import json
from django.shortcuts import render
import os
import slack
from dotenv import load_dotenv
from django.http import HttpResponse
from . import strings
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# Defining what html file to return when this function is called.

def fridge(request):

    r = requests.get('http://localhost:8000/api/fridges/')

    json_data = json.loads(r.text)
    data_list = []

    for i in json_data:
        a = ''
        if i['fridge_is_empty'] == True:
            a = 'Empty'
        else:
            a = 'Full'
        dict = {
            'id': i['id'],
            'name': i['name'],
            'state': a,
        }

        data_list.append(dict)
    context = {
        'data_list': data_list
    }

    return render(request, 'frontend/fridge.html', context)


def manage(request):
    return render(request, 'frontend/index.html')


# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))


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


@csrf_exempt
def test_method(request):
    if request.method == "POST":
        r = requests.get('http://localhost:8000/api/fridges/')
        json_data = json.loads(r.text)

        names = []
        states = []
        empty = 'Tyhjä'
        full = 'Täynnä'

        for i in json_data:
            names.append(i['name'])
            if i['fridge_is_empty'] == True:
                states.append(empty)
            else:
                states.append(full)

        zipObj = zip(names, states)
        dict1 = dict(zipObj)

        # Text formatting in SLACK
        str1 = ''.join(['```%s : %s``` \n' % (key, value)
                        for (key, value) in dict1.items()])
        client.chat_postMessage(
            channel=strings.CHANNEL_NAME_1,
            text=str(str1)
        )
    return HttpResponse("ok")
