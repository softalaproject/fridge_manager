import os
import slack
from . import utils
from dotenv import load_dotenv
from fridges.models import Fridge
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect


# Gets slack token from .env file and sets it here
load_dotenv()
slack_client = slack.WebClient(token=os.getenv("SLACK_TOKEN"))


def fridges(request):
    """ View for /fridges/ endpoint, uses create_list() passing the received request to it and then passing the filtered
    list as context to the template fridges.html """
    floor = request.GET.get('floor')
    id = request.GET.get('id')
    state = request.GET.get('state')

    context = {
        'data': utils.create_json_data_string(floor, id, state)
    }
    return render(request, 'frontend/fridges.html', context)


def json_view(request):
    """ view found at /api/json/ uses the create_list function, meaning it can use all the parameters listed in
    the function  """
    floor = request.GET.get('floor')
    fridge_id = request.GET.get('id')
    state = request.GET.get('state')

    filtered_string = utils.create_json_data_string(floor, fridge_id, state)
    json_response = utils.create_json(filtered_string)
    return HttpResponse(json_response)


def floors(request):
    """ View for index and /floors/ endpoint, passes create_floor_list() which creates a list of unique floors
     and passes it as context to template floors.html """
    context = {
        'data': utils.create_floor_list(),
    }
    return render(request, 'frontend/floors.html', context)


@csrf_exempt
def change_state(request):
    """ View for endpoint /api/change_state, which is used to change the state of a fridge and send
    the message to slack """
    # If the requests method which is sent to the endpoint is POST goes into the if logic
    # otherwise redirects back to where the user came from
    if request.method == 'POST':
        fridge_name = request.POST.get('name')
        fridge_id = request.POST.get('id')
        floor_id = request.POST.get('floor')
        channel = request.POST.get('channel')
        username_c = 'Floor: ' + floor_id + ', ' + fridge_name
        new_state = request.POST.get('new_state')

        # updates the fridge objects data in the database with given parameters
        Fridge.objects.filter(id=fridge_id).update(state=new_state)
        slack_client.chat_postMessage(
            channel=f'#{channel}',
            text=f'State: {new_state}',
            username=username_c
        )
    # redirects the requests sender back to where they came from
    # doesnt work if the user has blocked metadata with incognito mode or other means
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
