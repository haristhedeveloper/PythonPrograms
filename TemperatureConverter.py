
# In this we convert temperature from Celcius to Farenheit
# First we take temperature from the user into Celcius


tempCel= float(input("Enter the temperature into Celcius: "))

tempFar= (tempCel * 9/5) + 32  # Formula to convert celcius into Fahrenheit
print("Temperature in Fahrenheit is :",tempFar,"°F")