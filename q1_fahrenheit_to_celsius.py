#q1_fahrenheit_to_celsius.py
#Fahrenheit to celsius calculator

#Welcome Message

print("Welcome to Fahrenheit to Celsius calculator,")

#get input variables

fahrenheit=float(input("Please enter Fahrenheit value:"))

#compute temperature in celsius

celsius = float((5/9) * (fahrenheit - 32))

print("Celsius value is: {0:.2f}".format(celsius))
