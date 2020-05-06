from rest_framework import routers
from .api import FridgeViewSet
from django.urls import path, re_path
from django.conf.urls import url

url(r'^(?P<version>(v1))/fridges/$', views.fridges.as_view()),
re_path(r'^(?P<version>(v1))/fridges/(?P<pk>\d+)/$', views.fridges.as_view()),

router = routers.DefaultRouter()
# registers the api/fridges endpoint and maps it to use FridgeViewSet
router.register('api/fridges', FridgeViewSet, 'fridges')

urlpatterns = router.urls
