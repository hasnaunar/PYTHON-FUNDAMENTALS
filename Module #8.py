#Functions in Python

#Function to convert Fahrenheit to Celsius
def temp(F):
    return (F - 32) * 5 / 9

print(temp(77)) # Output in Celsius


# Function to convert Celsius to Fahrenheit
def cel(c):
    return c * 9 / 5 + 32

print(cel(77))  # Output in Fahrenheit
