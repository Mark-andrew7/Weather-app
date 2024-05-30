"""
Module that converts django module instances to json representations
"""

from rest_framework import serializers
from wise.models import Temperature, Wind

class TemperatureSerializer(serializers.ModelSerializer):
    """
    Converts temp model instances to json format
    """
    class Meta:
        model = Temperature
        fields = '__all__'

class WindSerializer(serializers.ModelSerializer):
    """
    Converts wind model instances to json format
    """
    class Meta:
        model = Wind
        fields = '__all__'
