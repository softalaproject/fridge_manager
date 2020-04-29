from .models import Fridge
from rest_framework import viewsets, permissions
from .serializers import FridgeSerializer


# FridgeViewSet defines which serializer to use for fridges and to return all fridge objects from database
class FridgeViewSet(viewsets.ModelViewSet):
    queryset = Fridge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FridgeSerializer
