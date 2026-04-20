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

class CardsModel(models.Model):

    name = models.CharField(max=200)
    card_type = models.TextChoices()
    description = models.TextField()
    type = models.Choices(CREATURE_TYPES)
    attack = models.IntegerField()
    defense = models.IntegerField()
    level = models.IntegerChoices()
    ra