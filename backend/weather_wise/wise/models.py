from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

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
