from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class CardType(models.TextChoices):
    NORMAL_MONSTER = "normal_monster", "Normal Monster"
    EFFECT_MONSTER = "effect_monster", "Effect Monster"
    FUSION_MONSTER = "fusion_monster", "Fusion Monster"
    RITUAL_MONSTER = "ritual_monster", "Ritual Monster"
    SPELL = "spell", "Spell"
    TRAP = "trap", "Trap"

class MonsterAttribute(models.TextChoices):
    LIGHT = "light", "LIGHT"
    DARK = "dark", "DARK"
    EARTH = "earth", "EARTH"
    WATER = "water", "WATER"
    FIRE = "fire", "FIRE"
    WIND = "wind", "WIND"
    DIVINE = "divine", "DIVINE"

class MonsterType(models.TextChoices):
    AQUA = "aqua", "Aqua"
    BEAST = "beast", "Beast"
    BEAST_WARRIOR = "beast_warrior", "Beast-Warrior"
    DINOSAUR = "dinosaur", "Dinosaur"
    DRAGON = "dragon", "Dragon"
    FAIRY = "fairy", "Fairy"
    FIEND = "fiend", "Fiend"
    FISH = "fish", "Fish"
    INSECT = "insect", "Insect"
    MACHINE = "machine", "Machine"
    PLANT = "plant", "Plant"
    PSYCHIC = "psychic", "Psychic"
    PYRO = "pyro", "Pyro"
    REPTILE = "reptile", "Reptile"
    ROCK = "rock", "Rock"
    SEA_SERPENT = "sea_serpent", "Sea Serpent"
    SPELLCASTER = "spellcaster", "Spellcaster"
    THUNDER = "thunder", "Thunder"
    WARRIOR = "warrior", "Warrior"
    WINGED_BEAST = "winged_beast", "Winged Beast"
    DIVINE_BEAST = "divine_beast", "Divine-Beast"
    ZOMBIE = "zombie", "Zombie"
    CYBERSE = "cyberse", "Cyberse"
    WYRM = "wyrm", "Wyrm"

class Rarity(models.TextChoices):
    COMMON = "common", "Common"
    RARE = "rare", "Rare"
    SUPER_RARE = "super_rare", "Super Rare"
    ULTRA_RARE = "ultra_rare", "Ultra Rare"
    SECRET_RARE = "secret_rare", "Secret Rare"


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

    class Meta:
        ordering = ["name"]
        verbose_name = "carta"
        verbose_name_plural = "cartas"

    def __str__(self):
        return self.name
