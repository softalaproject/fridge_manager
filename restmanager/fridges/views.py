from rest_framework import serializers
from requests import request
from . import FridgeSerializer
from django.http import Response, Http404


# Create your views here.
print("request.version: ", request.version)

class fridges(APIView):

   """
   List all Fridges.
   """

   def get(self, request, *args, **kwargs):
       #print("version:", request.version)
       queryset = fridges.objects.all()
       resultSet = FridgeSerializer(queryset, many=True)

       return Response(resultSet.data)

class FridgeDetails(APIView):

   """
   Retrieve a Fridge instance.
   """

   def get_object(self, pk):
       try:
           return fridges.objects.get(pk=pk)
       except fridges.DoesNotExist:
           raise Http404

   def get(self, request, *args, **kwargs):
       #print("version:",kwargs['version'])
       pk = kwargs['pk']
       fridge = self.get_object(pk)
       serializer = FridgeSerializer(fridge)

       return Response(serializer.data)