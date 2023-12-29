def convertToCelsius(deg_fahrenheit):
    return (deg_fahrenheit - 32) * (5 / 9)


def convertToFahrenheit(deg_celsius):
    return deg_celsius * (9 / 5) + 32


assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
assert convertToCelsius(convertToFahrenheit(15)) == 15

print(convertToCelsius(0))
print(convertToCelsius(180))
print(convertToFahrenheit(0))
print(convertToFahrenheit(100))
print(convertToCelsius(convertToFahrenheit(15)))
print(convertToCelsius(convertToFahrenheit(15)))
