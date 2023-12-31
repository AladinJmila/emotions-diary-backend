from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class EmotionalState(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    energy = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    intensity = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    triggers = models.TextField()
    coping_mechanisms = models.TextField()
    tags = models.TextField()
