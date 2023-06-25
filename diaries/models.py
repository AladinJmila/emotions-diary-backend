from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class EmotionalState(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    energy = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    intensity = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    triggers = models.TextField()
    coping_mechanism = models.TextField()
