from django.db import models

# Create your models here.

class Temperature(models.Model):
    """
    Represents the Temp class
    """
    value = models.FloatField(null=False)
    unit = models.CharField(max_length=1, default='C')

    def __str__(self):
<<<<<<< HEAD
        return self.name
=======
        return f"{self.value} {self.unit}"

class Wind(models.Model):
    """
    Represents the wind class
    """
    speed = models.FloatField()
    direction = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.speed} m/s {self.direction}"
>>>>>>> 60a06d3df08d7e13d89a625c8364e80eaad018df
