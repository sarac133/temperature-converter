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


if __name__ == "__main__":
    # Quick test of conversion functions
    print("Temperature Converter Tests")
    print(f"0°C = {celsius_to_fahrenheit(0)}°F")
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"0°C = {celsius_to_kelvin(0)}K")
