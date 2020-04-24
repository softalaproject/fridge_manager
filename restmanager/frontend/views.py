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
from rest_framework import generics
from fridges.serializers import FridgeSerializer


# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

IP2 = os.getenv('IP2')


class FloorList(generics.ListAPIView):
    serializer_class = FridgeSerializer

    def get_queryset(self):
        queryset = Fridge.objects.all()
        fid = self.request.query_params.get('id', None)

        if id is not None:
            queryset = queryset.filter(id=fid)
        return queryset


# Endpoint http://localhost:8069/fridges.
@csrf_exempt
def fridges(request):
    r = requests.get('HTTP://' + IP2 + ':8069/api/fridges/?format=json')
    data = json.loads(r.text)
    data_dict = []
    floor = request.GET.get('floor')
    print(type(floor))
    print(f'A floor is {floor}')
    if floor is not None:
        int_floor = int(floor)
        print(int_floor)
    else:
        int_floor = floor
        pass

    if floor is not None:
        print(f'B floor is {floor}')
        for item in data:
            dicti = {
                'id': item['id'],
                'name': item['name'],
                'state': item['state'],
                'floor': item['floor'],
            }
            if item['floor'] == int_floor:
                data_dict.append(dicti)
                print(f'C floor is {int_floor}')
            else:
                pass
    else:
        print(f'D floor is {floor}')
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
#     r = requests.get('HTTP://' + IP2 + ':8069/api/fridges/1/?format=json')
#     data = json.loads(r.text)
#     data_dict = []
#     for item in data:
#         dicti = {
#             'id': item['id'],
#             'name': item['name'],
#             'state': item['state'],
#             'floor': item['floor'],
#         }
#
#         data_dict.append(dicti)
#
#     context = {
#         'data': data_dict,
#     }
    return render(request, 'frontend/fridge.html')# , context)


@csrf_exempt
def create_fridges(request):
    fridge_1 = Fridge(name="Sauna Fridge", state="Empty", floor="1")
    fridge_2 = Fridge(name="Fridge", state="Full", floor="2")
    fridge_3 = Fridge(name="Fridgey", state="Half-full", floor="3")
    fridge_4 = Fridge(name="Fridgex", state="Half-full", floor="4")
    fridge_5 = Fridge(name="Fridgexy", state="Half-full", floor="5")
    fridge_6 = Fridge(name="Fridgeyx", state="Half-full", floor="6")
    fridge_7 = Fridge(name="Fridgeyxy", state="Half-full", floor="7")

    fridge_1.save()
    fridge_2.save()
    fridge_3.save()
    fridge_4.save()
    fridge_5.save()
    fridge_6.save()
    fridge_7.save()

    return HttpResponse("Created fridges.")


@csrf_exempt
def create_fridges2(request):
    fridge_1 = Fridge(name="Egdirf_01", state="Empty", floor="1")
    fridge_2 = Fridge(name="Egdirf_02", state="Full", floor="2")
    fridge_3 = Fridge(name="Egdirf_03", state="Half-full", floor="3")
    fridge_4 = Fridge(name="Egdirf_04", state="Half-full", floor="4")
    fridge_5 = Fridge(name="Egdirf_05", state="Half-full", floor="5")
    fridge_6 = Fridge(name="Egdirf_06", state="Half-full", floor="6")
    fridge_7 = Fridge(name="Egdirf_07", state="Half-full", floor="7")

    fridge_1.save()
    fridge_2.save()
    fridge_3.save()
    fridge_4.save()
    fridge_5.save()
    fridge_6.save()
    fridge_7.save()

    return HttpResponse("Created fridges 2.")


