from django.db import models
import math


class Temperature():
    """
    Representation of temp
    """
    value = models.FloatField(null=False)
    unit = models.CharField(max_length=1, default='C')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.unit not in ['C', 'F']:
            raise ValueError("Unit must be C or F")

    def convert_temp(self, target_unit):
        """
        Converts from Celcius to Farenheit and viceversa
        """
        if self.unit == target_unit:
            return self.value
        elif self.unit == 'C' and target_unit == 'F':
            return self.value * 9 / 5 + 32
        elif self.unit == 'F' and target_unit == 'C':
            return (self.value - 32) * 5 / 9
        else:
            raise ValueError(f"Unsupported unit conversion from {self.unit} to {target_unit}")
        
    def __str__(self):
        """
        Returns both value and its unit
        """
        return f"{self.value} {self.unit}"

class Wind(models.Model):
    """
    Represents the class wind
    """
    speed = models.FloatField()
    direction = models.CharField(max_length=3)

    def speed_kmh(self):
        """
        Converts speed to km/h from m/s
        """
        return self.speed * 3.5
    
    def validate_direction(self):
        """
        Validates wind direction in degrees or compass points
        """
        directions = ["N", "NE", "NW", "S", "SW", "SE", "E", "W"]
        if self.direction not in directions and not (0 <= int(self.direction) <= 360):
            raise ValueError(f"Invalid wind direction: {self.direction}")
    
    def descriptive_direction(self):
        """
        Returns human readable wind direction
        """
        compass_points = {
            "N": "North", "NE": "Northeast", "NW": "Northwest", "E": "East",
            "S": "South", "SE": "Southeast", "SW": "Southwest", "W": "West"
        }
        return compass_points.get(self.direction, f"{self.direction} degrees")
