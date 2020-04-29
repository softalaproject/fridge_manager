from django.db import models

# Create your models here.
# id, name, state, floor


class Fridge(models.Model):
    name = models.CharField(max_length=100, unique=True, default="Fridge ", editable="True")
    state = models.CharField(max_length=20, default='Empty', editable=True)
    floor = models.IntegerField(default=1)
    channel_msg = models.CharField(max_length=30, default='general', editable=True)

    def _str_(self):
        return self.name
