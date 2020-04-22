from django.db import models

# Create your models here.
# id, name, state, floor


class Fridge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    state = models.CharField(max_length=20)
    floor = models.IntegerField()

