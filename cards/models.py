from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from constants import MonsterAttribute, MonsterType, CardType, Rarity

class Card(models.Model):

    name = models.CharField("nome", max_length=200)
    card_type = models.CharField("tipo de carta", max_length=32, choices=CardType.choices)
    attribute = models.CharField(
        "atributo",
        max_length=16,
        choices=MonsterAttribute.choices,
        blank=True,
    )
    monster_type = models.CharField(
        "tipo de monstro",
        max_length=32,
        choices=MonsterType.choices,
        blank=True,
    )
    description = models.TextField("descrição / efeito", blank=True)
    attack = models.PositiveSmallIntegerField(
        "ATK",
        null=True,
        blank=True,
        validators=[MaxValueValidator(9999)],
    )
    defense = models.PositiveSmallIntegerField(
        "DEF",
        null=True,
        blank=True,
        validators=[MaxValueValidator(9999)],
    )
    level = models.PositiveSmallIntegerField(
        "nível / rank",
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(13)],
    )

    rarity = models.CharField(
        "raridade",
        max_length=32,
        choices=Rarity.choices,
        default=Rarity.COMMON,
    )

    card_image = models.ImageField("imagem", upload_to="cards/", blank=True, null=True)

    def __str__(self):
        return self.name
