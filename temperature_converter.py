def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
temp1 = float(input('Enter temperature in fahrenheit: '))
print(fahrenheit_to_celsius(temp1))

def describe_weather(celsius):
    if celsius < 0:
        return 'Freezing'
    elif celsius >= 0 and celsius <= 14.99:
        return 'Cold'
    elif celsius >= 15 and celsius <= 24.99:
        return 'Mild'
    else:
        return 'Hot'
temperature = describe_weather(fahrenheit_to_celsius(temp1))
print(f'The weather is: {temperature}:.2f')