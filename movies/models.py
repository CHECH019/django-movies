from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(null=True, blank=True, default=0,validators=[MinValueValidator(0), MaxValueValidator(5)])
    country = models.CharField(max_length=30)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)