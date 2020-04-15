from rest_framework import routers
from .api import FridgeViewSet, MessageViewSet, NewFridgeViewSet

router = routers.DefaultRouter()
router.register('api/fridges', FridgeViewSet, 'fridges')
router.register('api/messages', MessageViewSet, 'messages')
router.register('api/items', NewFridgeViewSet, 'items')

urlpatterns = router.urls
