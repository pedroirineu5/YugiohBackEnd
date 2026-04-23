from django.db import models
from cards.models import Card

class Packs(models.Model):

    package_name = models.CharField(max_length=200)
    package_cards = models.ManyToManyField(Card, related_name="packs")
    url_photo = models.URLField()
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    unlock = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.package_name