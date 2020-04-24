from rest_framework import serializers
from .models import Fridge

# Fridge Serializer
class FridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fridge
<<<<<<< HEAD
        fields = '__all__'


class Fridge2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        fields = '__all__'
=======
        fields = '__all__'
>>>>>>> dev
