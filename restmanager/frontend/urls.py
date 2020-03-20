from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/beeer/', views.beeer),
    path('api/nobeer/', views.nobeer),
    path('fridge',views.fridge)
]