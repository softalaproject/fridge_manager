from django.shortcuts import render
from rest_framework import viewsets
import os
import slack
from dotenv import load_dotenv
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from . import strings

# Create your views here.


def manage(request):
    return render(request, 'frontend/index.html')


def beer_response(request):
    return render(request, 'frontend/beer.html')


def no_beer_response(request):
    return render(request, 'frontend/no_beer.html')


def fridge(request):
    return render(request, 'frontend/fridge.html')


# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))


# Beer function
def beer(request):
    client.chat_postMessage(
        channel=strings.CHANNEL_NAME_1,
        text=strings.SLACKMESSAGE_3
    )
    messages.success(request, strings.SUCCESS_MSG_3)
    return HttpResponse(beer_response(request))


def no_beer(request):
    client.chat_postMessage(
        channel=strings.CHANNEL_NAME_1,
        text=strings.SLACKMESSAGE_1
    )
    messages.success(request, strings.SUCCESS_MSG_1)
    return HttpResponse(no_beer_response(request))

# Another beer function


def another_beer(request):
    client.chat_postMessage(
        channel=strings.CHANNEL_NAME_2,
        text=strings.SLACKMESSAGE_2
    )
    messages.success(request, strings.SUCCESS_MSG_2)
    return JsonResponse({'success': True})
