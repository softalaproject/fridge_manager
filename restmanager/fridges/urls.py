from rest_framework import routers
from .api import FridgeViewSet, Fridge2ViewSet

router = routers.DefaultRouter()
router.register('api/fridges', FridgeViewSet, 'fridges')
router.register('api/fridges2', Fridge2ViewSet, 'fridges2')

urlpatterns = router.urls
