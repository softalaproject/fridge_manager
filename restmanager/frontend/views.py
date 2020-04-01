import requests
import json
from django.shortcuts import render, redirect
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
        empty_checker = 0
        length = 0
        empty_ones = []

        for i in json_data:
            if i['fridge_is_empty'] == True:
                empty_checker += 1
                length += 1
                empty_ones.append(i['name'])
            else:
                length += 1

            names.append(i['name'])

            if i['fridge_is_empty'] == True:
                states.append(empty)
            else:
                states.append(full)

        zipObj = zip(names, states)
        dict1 = dict(zipObj)

        if empty_checker == 0:
            str2 = '*Kaikki jääkaapit täynnä!*'
        elif empty_checker/length < 0.5:
            str2 = f'Osa jääkaapeista on tyhjiä *{empty_ones}*'
        elif empty_checker/length < 1:
            str2 = f'Suurin osa jääkaapeista on tyhjiä *{empty_ones}*'
        else:
            str2 = f'Kaikki jääkapit ovat tyhjiä *{empty_ones}*'
            # Text formatting in SLACK
        str1 = ''.join(['```%s : %s``` \n' % (key, value)
                        for (key, value) in dict1.items()])
        client.chat_postMessage(
            channel=strings.CHANNEL_NAME_1,
            text=str(str1 + str2)
        )
    return HttpResponse("ok")


def update(request, id):
    if request.method == 'PUT':
        url = 'http://localhost:8000/api/fridges/'+id
        r = requests.get(url)
        json_data = json.loads(r.text)

        if json_data['fridge_is_empty'] == True:
            s = requests.put(url, data={'fridge_is_empty': False})
            print(s)
        elif json_data['fridge_is_empty'] == False:
            s = requests.put(url, data={'fridge_is_empty': True})
            print(s)

    return redirect('')
