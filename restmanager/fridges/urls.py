from rest_framework import routers
from .api import FridgeViewSet

router = routers.DefaultRouter()
# registers the api/fridges endpoint and maps it to use FridgeViewSet
router.register('api/fridges', FridgeViewSet, 'fridges')

urlpatterns = router.urls
