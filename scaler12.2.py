#programto convert celsius to fahrenheit
def celsius_to_fahrenheit(celsius):
    ans=(celsius*1.8)+32# formula
    return round(ans,2)#rounding

print(celsius_to_fahrenheit(36.8))