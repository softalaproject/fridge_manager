import json
from fridges.models import Fridge


def values_queryset_to_dict(vqs):
    return [item for item in vqs]


def create_json(dicti):
    """ converts given dict into json and returns it as a string"""
    json_string = json.dumps(dicti)
    return json_string


def create_json_data_string(floor = None, id = None, state = None):
    """ Accepts parameters if found in url, filters data based on found parameter or returns data which contains
    all fridge object models values in the database """
    data = Fridge.objects.all().values().order_by('floor')
    # Checks if params exist in request
    if floor is not None:
        data = data.filter(floor=floor)
    elif id is not None:
        data = data.filter(id=id)
    elif state is not None:
        state = state.capitalize()
        data = data.filter(state=state).order_by('floor')
    data_dict = values_queryset_to_dict(data)
    data_json = json.dumps(data_dict)
    return json.loads(data_json)


def create_uniq_floors():
    """ queryset with distinct floors """
    floors = Fridge.objects.all().values_list('floor', flat=True).distinct().order_by('floor')
    data_dict = values_queryset_to_dict(floors)
    floors_json = json.dumps(data_dict)
    return json.loads(floors_json)


def create_floor_list():
    """ Creates a list of unique floors found in fridges table in the database and returns it """
    floor_list = []
    for item in create_uniq_floors():
        floor_list.append(item)
    return floor_list
