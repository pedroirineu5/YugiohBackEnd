from cards.serializers import CardsSerializers
from rest_framework import generics
from cards.models import Card

class CardCreateList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardsSerializers

class CardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardsSerializers