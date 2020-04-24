from django.urls import path
from . import views


# Defining URL endpoints and what views they should return.
urlpatterns = [
    path('', views.fridges, name="home"),
    path('fridges', views.fridges),
    path('fridges/', views.fridges),
    path('api/change_state/', views.change_state),
    path('create_fridges/', views.create_fridges),
    path('create_fridges2/', views.create_fridges2),
]
