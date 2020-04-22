from django.contrib import admin
from .models import Fridge
# Register your models here.
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'floor')

admin.site.register(Fridge, AppAdmin)