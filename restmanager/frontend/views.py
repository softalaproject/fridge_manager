from django.shortcuts import render
from rest_framework import viewsets
import os
import slack
from dotenv import load_dotenv
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from . import strings

# Create your views here.


# Defining what html file to return when this function is called.

def fridge(request):
    return render(request, 'frontend/fridge.html')


def no_beer_response(request):
    return render(request, 'frontend/no_beer.html')


def beer_response(request):
    return render(request, 'frontend/beer.html')


def manage(request):
    return render(request, 'frontend/index.html')


# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))


# Defining what the view at no_beer.html does
def no_beer(request):
    client.chat_postMessage(
        channel=strings.CHANNEL_NAME_1,
        text=strings.SLACKMESSAGE_1
    )
    return HttpResponse(no_beer_response(request))


# Defining what the view at beer.html does
def beer(request):
    # Sending message to slack, message contents imported from strings.py
    client.chat_postMessage(
        channel=strings.CHANNEL_NAME_1,
        text=strings.SLACKMESSAGE_2
    )
    # returning HttpResponse defined in function beer_response
    return HttpResponse(beer_response(request))
