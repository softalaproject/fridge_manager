from django.urls import path
from . import views, urlfunctions


# Defining URL endpoints and what views they use.
urlpatterns = [
    path('', views.floors, name="home"),
    path('fridges', views.fridges),
    path('fridges/', views.fridges),
    path('api/change_state/', urlfunctions.change_state),
    path('api/json/', views.json_view),
    path('floors', views.floors),
    path('floors/', views.floors),
    path('create_fridges', urlfunctions.create_fridges),
]
