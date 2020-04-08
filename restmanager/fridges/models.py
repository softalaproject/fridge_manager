from django.db import models

# Create your models here.
# Fridgename, Fridgelevel, Fridgelevel_is_empty, Fridge_time_since,


class Fridge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    fridge_is_empty = models.BooleanField()
    time_since = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    msg = models.CharField(max_length=1000)


class NewFridge(models.Model):
    name = models.CharField(max_length=100, unique=True)
    state = models.CharField(max_length=20)
