from .models import Fridge, Message
from rest_framework import viewsets, permissions
from .serializers import FridgeSerializer, MessageSerializer

# Fridge Viewset


class FridgeViewSet(viewsets.ModelViewSet):
    queryset = Fridge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FridgeSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MessageSerializer
