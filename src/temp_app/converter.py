"""
Temperature Converter Module
Provides functions to convert between Celsius, Fahrenheit, and Kelvin.
"""

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """
    Convert temperature from Celsius to Kelvin.
    """
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    """
    return kelvin - 273.15

def celsius_to_rankine(celsius):
    """
    Convert temperature from Celsius to Rankine.
    Formula: Rankine = (Celsius + 273.15) × 9/5
    """
    kelvin = celsius_to_kelvin(celsius)
    return kelvin * 9/5


def rankine_to_celsius(rankine):
    """
    Convert temperature from Rankine to Celsius.
    Formula: Celsius = (Rankine × 5/9) - 273.15
    """
    kelvin = rankine * 5/9
    return kelvin_to_celsius(kelvin)



if __name__ == "__main__":
    print("Temperature Converter Tests")
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"0°C = {celsius_to_kelvin(0)}K")
    print(f"0°C = {celsius_to_rankine(0)}°R")
    print(f"491.67°R = {rankine_to_celsius(491.67)}°C")
