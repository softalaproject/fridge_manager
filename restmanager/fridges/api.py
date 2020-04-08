from .models import Fridge, Message, NewFridge
from rest_framework import viewsets, permissions
from .serializers import FridgeSerializer, MessageSerializer, NewFridgeSerializer

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


class NewFridgeViewSet(viewsets.ModelViewSet):
    queryset = NewFridge.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewFridgeSerializer
