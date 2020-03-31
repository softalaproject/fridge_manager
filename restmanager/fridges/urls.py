from rest_framework import routers
from .api import FridgeViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register('api/fridges', FridgeViewSet, 'fridges')
router.register('api/messages', MessageViewSet, 'messages')

urlpatterns = router.urls
