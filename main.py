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