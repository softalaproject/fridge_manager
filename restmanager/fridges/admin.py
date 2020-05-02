from django.contrib import admin
from .models import Fridge


# Register your models here.
class AppAdmin(admin.ModelAdmin):
    # defines what fields to show in the admin view
    list_display = ('name', 'state', 'floor', 'channel')


# registers the fridge model to admin.site
admin.site.register(Fridge, AppAdmin)
