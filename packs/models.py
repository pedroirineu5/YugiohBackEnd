from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from cards.models import Card


class Pack(models.Model):
    """Pacote de cartas à venda ou desbloqueável no jogo."""

    name = models.CharField("nome", max_length=200, db_index=True)
    cards = models.ManyToManyField(
        Card,
        related_name="packs",
        verbose_name="cartas",
        blank=True,
    )
    cover_url = models.URLField("URL da capa", max_length=500)

    price = models.PositiveIntegerField(
        "preço",
        validators=[MinValueValidator(50), MaxValueValidator(9999)],
    )
    description = models.TextField("descrição", blank=True)

    unlock_requirements = models.TextField(
        "requisitos de desbloqueio",
        blank=True,
        help_text="Texto livre: como o jogador desbloqueia ou obtém este pacote.",
    )

    def __str__(self):
        return self.name
