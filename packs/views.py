from django.shortcuts import render

from rest_framework import generics

from packs.serializers import PacksSerializers
from packs.models import Packs

class PacksCreateListView(generics.ListCreateAPIView):
    queryset = Packs.objects.all()
    serializer_class = PacksSerializers

class PacksRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Packs.objects.all()
    serializer_class = PacksSerializers
