from django.urls import path
from . import views

# Defining URL endpoints and what views they should return.
urlpatterns = [
    path('', views.fridge, name="home"),
    path('items', views.items),
    path('manage', views.manage),
    path('api/beer/', views.post_beer, name="full"),
    path('api/no_beer/', views.post_no_beer, name="empty"),
    path('fridge', views.fridge),
	path('fridge2', views.fridge2),
    path('api/test_method/', views.test_method),
    path('api/change_method/', views.change_method),
    path('api/change_to_empty/', views.change_to_empty),
    path('api/change_item/', views.change_item),

]
