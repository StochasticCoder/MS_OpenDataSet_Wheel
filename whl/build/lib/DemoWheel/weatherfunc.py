## Convert celsius temp to fahrenheit
def celsius_to_fahrenheit(value):
    if value is None:
        return 0
    else:
        return (value * (9/5)) + 32