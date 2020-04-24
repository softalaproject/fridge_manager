from rest_framework import viewsets, permissions
from .serializers import FridgeSerializer
from .models import Fridge


# Fridge Viewset
class FridgeViewSet(viewsets.ModelViewSet):
    queryset = Fridge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FridgeSerializer
