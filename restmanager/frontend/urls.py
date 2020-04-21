from django.urls import path
from . import views

# Defining URL endpoints and what views they should return.
urlpatterns = [
    path('', views.items, name="home"),
    path('items', views.items),
    path('items/', views.items),
    path('api/beer/', views.post_beer, name="full"),
    path('api/no_beer/', views.post_no_beer, name="empty"),
    path('fridge', views.fridge),
    path('api/change_item/', views.change_item),
    path('create_fridges/', views.create_fridges),
]
