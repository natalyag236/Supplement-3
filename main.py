def celsius_to_fahrenheit(celsius):
    """convert a temperature from celsius to fahrenheit

    Args:
        celsius (float): the temperature in degrees celsius

    Returns:
        float: the temperature converted to degrees fahrenheit
    """
    return (celsius * 9/5 ) + 32

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(100) == 212

def fahrenheit_to_celsius(fahrenheit):
    """converts a temperature form fahrenheit to celsius

    Args:
        fahrenheit (float): The temperature in degrees fahrenheit

    Returns:
        float: the temperature to degrees celsius
    """
    return (fahrenheit - 32) * 5/9

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0

def test_isEven():
  assert isEven(4) == True