from pydoc import describe
from django.db import models

CREATURE_TYPES = (
        ("aqua", "Aqua"),
        ("beast", "Beast"),
        ("beast_warrior", "Beast-Warrior"),
        ("dinosaur", "Dinosaur"),
        ("dragon", "Dragon"),
        ("fairy", "Fairy"),
        ("fiend", "Fiend"),
        ("fish", "Fish"),
        ("insect", "Insect"),
        ("machine", "Machine"),
        ("plant", "Plant"),
        ("psychic", "Psychic"),
        ("pyro", "Pyro"),
        ("reptile", "Reptile"),
        ("rock", "Rock"),
        ("sea_serpent", "Sea Serpent"),
        ("spellcaster", "Spellcaster"),
        ("thunder", "Thunder"),
        ("warrior", "Warrior"),
        ("winged_beast", "Winged Beast"),
        ("divine_beast", "Divine-Beast"),
        ("zombie", "Zombie"),
        ("effect", "Effect"),
    )

CARD_TYPES = (
    ("normal_monster", "Normal Monster"),
    ("effect_monster", "Effect Monster"),
    ("fusion_monster", "Fusion Monster"),
    ("ritual_monster", "Ritual Monster"),
    ("spell", "Spell"),
    ("trap", "Trap"),
)

class CardsModel(models.Model):

    name = models.CharField(max=200)
    card_type = models.Choices(CARD_TYPES)
    type = models.Choices(CREATURE_TYPES)
    description = models.TextField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    level = models.IntegerChoices()
    rarity = models.IntegerField()

    def __str__(self):
        