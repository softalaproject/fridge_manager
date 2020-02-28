from rest_framework import routers
from fridges.api import FridgeViewSet

router = routers.DefaultRouter()
router.register('api/fridges', FridgeViewSet, 'fridges')

urlpatterns = router.urls