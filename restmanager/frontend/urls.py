from django.urls import path
from . import views

urlpatterns = [
    path('', views.fridge),
    path('manage', views.manage),
    path('api/beer/', views.beer),
    path('api/no_beer/', views.no_beer),
    path('fridge', views.fridge)
]