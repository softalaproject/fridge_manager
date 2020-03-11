from django.shortcuts import render
from rest_framework import viewsets
import os
import slack
from dotenv import load_dotenv
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'frontend/index.html')


# GET SLACK TOKEN HERE
load_dotenv()
client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))

# Beer function


def nobeer(request):
    client.chat_postMessage(
        channel='#general',
        text="Saunatilasta on juomat loppu. Haeppa lisää!"
    )
    messages.success(request, 'Viesti lähetetty Slack-kanavalle')
    return JsonResponse({'success': True})

# Another beer function


def another_beer(request):
    client.chat_postMessage(
        channel="#general",
        text="Beer is out"
    )
    messages.success(request, 'Message sent')
    return JsonResponse({'success': True})
