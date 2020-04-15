from django.urls import path
from . import views

# Defining URL endpoints and what views they should return.
urlpatterns = [
    path('', views.fridge2),
    path('manage', views.manage),
    path('api/beer/', views.post_beer),
    path('api/no_beer/', views.post_no_beer),
    path('fridge', views.fridge2),
]