
from rest_framework import serializers
from cards.models import Card

class CardsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Card
        field = '__all__'