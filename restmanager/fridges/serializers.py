from rest_framework import serializers
from .models import Fridge, Message, NewFridge

# Fridge Serializer


class FridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class NewFridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewFridge
        fields = '__all__'
