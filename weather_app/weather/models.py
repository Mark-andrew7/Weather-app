from typing import Any
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
    
    @property
    def descriptive_direction(self):
        """
        Returns human readable wind direction
        """
        compass_points = {
            "N": "North", "NE": "Northeast", "NW": "Northwest", "E": "East",
            "S": "South", "SE": "Southeast", "SW": "Southwest", "W": "West"
        }
        return compass_points.get(self.direction, f"{self.direction} degrees")
    
    def calculate_wind_chill(self, temperature):
        """
        Calculates wind chill based on temp and wind speed
        """
        wind_speed = self.speed_kmh
        if temperature <= 10 and wind_speed >= 4.8:
            wind_chill = 13.12 + 0.6215 * temperature - 11.37 * math.pow(wind_speed, 0.16) + 0.3965 * temperature * math.pow(wind_speed, 0.16)
            return wind_chill
        return temperature
    
class Humidity(models.Model):
    """
    Represents the class Humidity
    """
    def __init__(self, relative_humidity=None):
        """
        Initializes the humidity class
        """
        self.relative_humidity = relative_humidity
    
    @property
    def humidity(self):
        """
        Getter method that retrieves humidity
        """
        return self._relative_humidity
    
    @humidity.setter
    def humidity_setter(self, value):
        """
        Setter method that sets humidity value
        """
        if value is not None and (value < 0 and value > 100):
            raise ValueError("Relative humidity must be between 0 and 100")
        self._relative_humidity = value