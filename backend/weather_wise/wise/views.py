from django.shortcuts import render
from .models import Temperature, Wind
from .utils import convert_temp, speed_kmh, descriptive_direction, calculate_wind_chill
import requests

def fetch_weather_data(location):
    # # Fetch the API key from settings
    api_key = settings.WEATHER_API_KEY

    # Make a request to the weather API
    response = requests.get('https://api.weatherapi.com/forecast', params={'q': location, 'key': api_key})

    # Process the API response
    if response.status_code == 200:
        data = response.json()
        current_condition = data['current']
        temperature_celcius = current_condition['temp_c']
        temperature_farenheit = convert_temp(temperature_celcius, 'C', 'F')
        wind_speed_mps = current_condition['wind_kmh'] / 3.6
        wind_speed_kmh = speed_kmh(wind_speed_mps)

        # Create and save Temperature instance
        temperature = Temperature.objects.create(value=temperature_celcius, unit='C')
        temperature.save()

        # Create and save Temperature instance
        wind = Wind.objects.create(speed=wind_speed_kmh)
        wind.save()

        return temperature, wind
    else:
        print('Failed to Fetch weather data')
        return None, None, None

def home(request):
    """
    Retrieve Temp and Wind data from database
    """
    temperature_data = Temperature.objects.all()
    wind_data = Wind.objects.all()

    temp_data = []
    for temp in temperature_data:
        temp_value_c = temp.value if temp.unit == 'C' else convert_temp(temp.value, temp.unit, 'C')
        temp_data.append({
            'value': temp.value,
            'unit': temp.unit,
            'value_c': temp_value_c,
            'value_f': convert_temp(temp.value, temp.unit, 'F'),
        })

    wind_data_list = []
    for wind in wind_data:
        speed_in_kmh = speed_kmh(wind.speed)
        wind_data_list.append({
            'speed_mps': wind.speed,
            'speed_kmh': speed_in_kmh,
            'direction': wi-nd.direction,
            'description': descriptive_direction(wind.direction),
            'wind_chill': calculate_wind_chill(temp_data[0]['value_c'], speed_in_kmh) if temp_data else None
        })

    context = {
        'temperature_data': temp_data,
        'wind_data': wind_data_list,
    }
    return render(request, 'home.html', context)
