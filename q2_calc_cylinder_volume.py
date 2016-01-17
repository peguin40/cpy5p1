#q2_calc_cylinder_volume.py
#Volume of cylinder calculator

#Welcome message

print("Welcome to Cylinder Volume Calculator, \n Please enter the following value(s):")

#get input variables

radius = float(input("Radius in cm: "))
length = float(input("Length in cm: "))

#compute volume

from math import pi 

base_area = float(radius * radius * pi)

volume = float(base_area * length)

#display result

print("The volume of the cylinder is: {0:.2f} cubic centimetres".format(volume))
