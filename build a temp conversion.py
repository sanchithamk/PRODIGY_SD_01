def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Conversion Program")
    
    # Prompt user for input
    temperature = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        print(f"{temperature}°C is equivalent to {fahrenheit:.2f}°F and {kelvin:.2f}K")
    
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        print(f"{temperature}°F is equivalent to {celsius:.2f}°C and {kelvin:.2f}K")
    
    elif unit == 'K':
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        print(f"{temperature}K is equivalent to {celsius:.2f}°C and {fahrenheit:.2f}°F")
    
    else:
        print("Invalid unit. Please enter C, F, or K.")

if __name__ == "__main__":
    main()
