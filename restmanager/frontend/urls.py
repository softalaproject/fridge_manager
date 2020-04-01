from django.urls import path
from . import views

# Defining URL endpoints and what views they should return.
urlpatterns = [
    path('', views.fridge),
    path('manage', views.manage),
    path('api/beer/', views.post_beer, name="full"),
    path('api/no_beer/', views.post_no_beer, name="empty"),
    path('fridge', views.fridge),
    path('api/test_method/', views.test_method),
    path('api/fridges/<id>/', views.update, name='update'),
]
