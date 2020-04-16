from django.shortcuts import render
import os
import slack
from dotenv import load_dotenv
from django.http import HttpResponse
from . import strings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


# Defining what html file to return when this function is called.

def fridge2(request):
    return render(request, 'frontend/fridge2.html')


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
