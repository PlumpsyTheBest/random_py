# Converts Celsius to Fahrenheit.
def celsius_to_fahrenheit(Celsius):
    Fahrenheit = Celsius*(9/5) + 32
    return Fahrenheit


# Main program loop for temperature conversion
if __name__ == "__main__":
    temperatureCelsius = 0
    while(temperatureCelsius != "q"):
        temperatureCelsius = input("What is the temperature in Celsius")
        if (temperatureCelsius != "q"):
            temperatureFahrenheit = celsius_to_fahrenheit(temperatureCelsius)
            print(temperatureFahrenheit)
        else:
            break

