from django.urls import path
from . import views

# Defining URL endpoints and what views they should return.
urlpatterns = [
    path('', views.fridges, name="home"),
    path('fridges', views.fridges),
    path('fridges/', views.fridges),
    path('fridge', views.fridge),
    path('api/beer/', views.post_beer, name="full"),
    path('api/no_beer/', views.post_no_beer, name="empty"),
    path('api/change_state/', views.change_state),
    path('create_fridges/', views.create_fridges),
]
