from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from wise.models import Temperature, Wind
from .serializers import TemperatureSerializer, WindSerializer
from wise.views import (convert_temp, speed_kmh, validate_direction, descriptive_direction, calculate_wind_chill)

# Create your views here.
class TemperatureViewSet(viewsets.ModelViewSet):
    """
    Viewset for handling temperature data
    """
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def retrieve(self):
        """
        Handle GET requests for individual temp instances
        """
        temp_inst = self.get_object()
        serializer = self.get_serializer(temp_inst)
        data = serializer.data
        data['converted'] = {
            'F': convert_temp(temp_inst.value, temp_inst.unit, 'F')if temp_inst.unit == 'C' else None,
            'C': convert_temp(temp_inst.value, temp_inst.unit, 'C')if temp_inst.unit == 'F' else None,
        }
        return Response(data)
    
class WindViewSet:
    """
    Viewset for handling wind data
    """
    queryset = Wind.objects.all()
    serializer_class = WindSerializer

    def retrieve(self):
        """
        Handle GET requests for individual wind instances
        """
        wind_inst = self.get_object()
        serializer = self.get_serializer(wind_inst)
        data = serializer.data
        return Response(data)
