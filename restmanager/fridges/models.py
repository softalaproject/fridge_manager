from django.db import models
from .defaultvars import name_def, state_def, floor_def, channel_def
# id, name, state, floor


class Fridge(models.Model):
    name = models.CharField(max_length=100, unique=True, default=name_def, editable=True)
    state = models.CharField(max_length=20, default=state_def, editable=True)
    floor = models.IntegerField(default=floor_def)
    channel_msg = models.CharField(max_length=30, default=channel_def, editable=True)

    def _str_(self):
        return self.name
