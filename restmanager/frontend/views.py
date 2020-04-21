import requests
import json
from django.shortcuts import render, redirect
import os
import slack
from dotenv import load_dotenv
from django.http import HttpResponse
from . import strings
from django.views.decorators.csrf import csrf_exempt
from fridges.models import NewFridge

# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

IP2 = os.getenv('IP2')


def full_fridge(request):
    r1 = requests.get('HTTP://' + IP2 + ':8000/api/items/?format=json')
    print(r1.text)
    fid = request.GET.get('id')
    NewFridge.objects.filter(id=fid).update(state='Full')
    r2 = requests.get('HTTP://' + IP2 + ':8000/api/items/?format=json')
    print(r2.text)
    return redirect('/items/') # HttpResponse(f"Fridge id: {id} Set to Full")


def half_fridge(request):
    r1 = requests.get('HTTP://' + IP2 + ':8000/api/items/?format=json')
    print(r1.text)
    fid = request.GET.get('id')
    NewFridge.objects.filter(id=fid).update(state='Half-full')
    r2 = requests.get('HTTP://' + IP2 + ':8000/api/items/?format=json')
    print(r2.text)
    return HttpResponse(f"Fridge id: {fid} Set to Half-full")


def empty_fridge(request):
    r1 = requests.get('HTTP://' + IP2 + ':8000/api/items/?format=json')
    print(r1.text)
    fid = request.GET.get('id')
    NewFridge.objects.filter(id=fid).update(state='Empty')
    r2 = requests.get('HTTP://' + IP2 + ':8000/api/items/?format=json')
    print(r2.text)
    return HttpResponse(f"Fridge id: {fid} Set to Empty.")


def create_fridges(request):
    a = NewFridge(name="fridge", state="Empty")
    b = NewFridge(name="fridgex", state="Full")
    c = NewFridge(name="fridgey", state="Half-full")
    a.save()
    b.save()
    c.save()
    return HttpResponse("Created fridges")


# Endpoint http://localhost:8000/items.
# Displays User Portal domain with a single item(fridge).
# and PUT command to communicate the state to slack channel.
@csrf_exempt
def items(request):
    t = requests.get('https://sauna.eficode.fi/get-latest')
    temp_data = json.loads(t.text)
    t_dict = []
    temp = round(temp_data['temperature'], 1)
    humid = round(temp_data['humidity'], 1)
    temps = {
        'temp': temp,
        'humid': humid
    }
    t_dict.append(temps)

    r = requests.get('HTTP://' + IP2 + ':8000/api/items/?format=json')
    data = json.loads(r.text)
    # print(r.text)
    data_dict = []

    for item in data:
        dicti = {
            'id': item['id'],
            'name': item['name'],
            'state': item['state']
        }

        data_dict.append(dicti)
    context = {
        'data': data_dict,
    }
    # print(data_dict)

    return render(request, 'frontend/items.html', context)


@csrf_exempt
def change_item(request):
    print(request.POST)
    '''
    docstring: put method to change fridge state
    '''
    if request.method == 'POST':
        # url = 'http://' + IP2 + ':8000/api/items/1/?format=json'
        # r = requests.get(url)
        # data = json.loads(r.text)
        # name = data['name']
        fid = request.POST.get('id')
        if request.POST.get('state') == 'Empty':
            new_state = 'Full'

        elif request.POST.get('state') == 'Full':
            new_state = 'Half'

        else:
            new_state = 'Empty'

        NewFridge.objects.filter(id=fid).update(state=new_state)
        # client.chat_postMessage(
        #     channel=strings.CHANNEL_NAME_1,
        #     text=str(str1)
        # )
    return redirect('/items')


# Endpoint http://localhost:8000/. Displays HTML page with jquery. found in templates -> fridge.html
def fridge(request):
    # r = requests.get('http://localhost:8000/api/fridges/?format=json')
    #
    # json_data = json.loads(r.text)
    # data_list = []
    #
    # for i in json_data:
    #     a = ''
    #     if i['fridge_is_empty']:
    #         a.lower = 'Empty'
    #     else:
    #         a = 'Full'
    #     dicti = {
    #         'id': i['id'],
    #         'name': i['name'],
    #         'state': a,
    #     }
    #
    #     data_list.append(dicti)
    # context = {
    #     'data_list': data_list
    # }
    return render(request, 'frontend/fridge.html')# , context)


def fridge2(request):
    return render(request, 'frontend/fridge2.html')


@csrf_exempt
def get_url_id(request):
    pass


@csrf_exempt
def change_to_empty(request):
    if request.method == 'POST':
        url_id = '26'
        url = f'http://localhost:8000/api/fridges/{url_id}/'
        r = requests.get(url)
        json_data = json.loads(r.text)

        if json_data.get('fridge_is_empty'):
            s = requests.put(url, data={
                'name': json_data['name'],
                'fridge_is_empty': False
            })
            print(s)
        else:
            s = requests.put(url, data={
                'name': json_data['name'],
                'fridge_is_empty': True
            })
            print(s)

    return HttpResponse("b")

# Endpoint http://localhost:8000/manage. Displays admin web domain powered by React.
def manage(request):
    return render(request, 'frontend/index.html')


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
            if i['fridge_is_empty']:
                empty_checker += 1
                length += 1
                empty_ones.append(i['name'])
            else:
                length += 1

            names.append(i['name'])

            if i['fridge_is_empty']:
                states.append(empty)
            else:
                states.append(full)

        zipObj = zip(names, states)
        dict1 = dict(zipObj)

        if empty_checker == 0:
            str2 = '*Kaikki jääkaapit täynnä!*'
        elif empty_checker / length < 0.5:
            str2 = f'Osa jääkaapeista on tyhjiä *{empty_ones}*'
        elif empty_checker / length < 1:
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


@csrf_exempt
def change_method(request):
    if request.method == 'POST':
        url = 'http://localhost:8000/api/fridges/27/'
        r = requests.get(url)
        json_data = json.loads(r.text)

        if json_data.get('fridge_is_empty'):
            s = requests.put(url, data={
                'name': json_data['name'],
                'fridge_is_empty': False
            })
            print(s)
        else:
            s = requests.put(url, data={
                'name': json_data['name'],
                'fridge_is_empty': True
            })
            print(s)

    return HttpResponse("b")


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
