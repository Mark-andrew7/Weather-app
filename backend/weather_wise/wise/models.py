from django.db import models

# Create your models here.

class Temperature(models.Model):
    """
    Represents the Temp class
    """
    value = models.FloatField(null=False)
    unit = models.CharField(max_length=1, default='C')

    def __str__(self):
        return f"{self.value} {self.unit}"

class Wind(models.Model):
    """
    Represents the wind class
    """
    speed = models.FloatField()
    direction = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.speed} m/s {self.direction}"
