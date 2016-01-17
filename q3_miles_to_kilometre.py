#q3_miles_to_kilometre.py
#miles to kilometre calculator

#Welcome Message
print("Welcome to Miles to Kilometre calculator, \n Please input the following value(s)")

#get input variable(s)
miles = float(input("Miles:"))

#compute kilometre value
kilometres = float(1.60934 * miles)

#display results
print("{0} miles in kilometres is {1:.3f}km(3dp)".format(miles,kilometres))
