
## TODO fix the constants for the choice models fields


class CardType(object):
    NORMAL_MONSTER = "normal_monster", "Normal Monster"
    EFFECT_MONSTER = "effect_monster", "Effect Monster"
    FUSION_MONSTER = "fusion_monster", "Fusion Monster"
    RITUAL_MONSTER = "ritual_monster", "Ritual Monster"
    SPELL = "spell", "Spell"
    TRAP = "trap", "Trap"

class MonsterAttribute(object):
    LIGHT = "light", "LIGHT"
    DARK = "dark", "DARK"
    EARTH = "earth", "EARTH"
    WATER = "water", "WATER"
    FIRE = "fire", "FIRE"
    WIND = "wind", "WIND"
    DIVINE = "divine", "DIVINE"

class MonsterType(object):
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

class Rarity(object):
    COMMON = "common", "Common"
    RARE = "rare", "Rare"
    SUPER_RARE = "super_rare", "Super Rare"
    ULTRA_RARE = "ultra_rare", "Ultra Rare"
    SECRET_RARE = "secret_rare", "Secret Rare"