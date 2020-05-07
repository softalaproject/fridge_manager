from rest_framework import serializers
from .models import Fridge


# Fridge Serializer for /api/fridges endpoint defines which fields to return and from which model
class FridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        fields = '__all__'

