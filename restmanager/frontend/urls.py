from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/beer/', views.nobeer)
]