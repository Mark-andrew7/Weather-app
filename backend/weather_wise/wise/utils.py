import math

def convert_temp(value, unit, target_unit):
    """
    Converts temperature from one unit to another (Celsius to Fahrenheit and vice versa).

    :param value: The temperature value to convert.
    :param unit: The current unit of the temperature ('C' for Celsius, 'F' for Fahrenheit).
    :param target_unit: The target unit to convert to ('C' or 'F').
    :return: The converted temperature value.
    :raises ValueError: If the target unit conversion is not supported.
    """
    if unit == target_unit:
        return value
    elif unit == 'C' and target_unit == 'F':
        return value * 9 / 5 + 32
    elif unit == 'F' and target_unit == 'C':
        return (value - 32) * 5 / 9
    else:
        raise ValueError(f"Unsupported unit conversion from {unit} to {target_unit}")

def speed_kmh(speed_mps):
    """
    Converts speed from meters per second (m/s) to kilometers per hour (km/h).

    :param speed_mps: Speed in meters per second.
    :return: Speed in kilometers per hour.
    """
    return speed_mps * 3.6

def validate_direction(direction):
    """
    Validates if the wind direction is either a valid compass point or a degree between 0 and 360.

    :param direction: The wind direction to validate.
    :raises ValueError: If the direction is not valid.
    """
    directions = ["N", "NE", "NW", "S", "SW", "SE", "E", "W"]
    if direction not in directions and not (0 <= int(direction) <= 360):
        raise ValueError(f"Invalid wind direction: {direction}")

def descriptive_direction(direction):
    """
    Converts a wind direction from compass points or degrees to a human-readable description.

    :param direction: The wind direction to describe.
    :return: A human-readable description of the wind direction.
    """
    compass_points = {
        "N": "North", "NE": "Northeast", "NW": "Northwest", "E": "East",
        "S": "South", "SE": "Southeast", "SW": "Southwest", "W": "West"
    }
    return compass_points.get(direction, f"{direction} degrees")

def calculate_wind_chill(temperature, speed_kmh):
    """
    Calculates the wind chill based on temperature and wind speed in km/h.

    :param temperature: The air temperature in Celsius.
    :param speed_kmh: The wind speed in kilometers per hour.
    :return: The calculated wind chill if applicable, otherwise the original temperature.
    """
    if temperature <= 10 and speed_kmh >= 4.8:
        wind_chill = 13.12 + 0.6215 * temperature - 11.37 * math.pow(speed_kmh, 0.16) + 0.3965 * temperature * math.pow(speed_kmh, 0.16)
        return wind_chill
    return temperature
