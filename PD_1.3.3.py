#Add functions for multiplication, division, and returning the polar coordinates of a number

import os
os.system('cls')

print("This program takes polar coordinates as input and gives back its product & division")
r1,phi1 = input("Please enter first polar coordinates in the form a,b : ").split(",")
r2,phi2 = input("Please enter first polar coordinates in the form a,b : ").split(",")

r1 = int(r1)
r2 = int(r2)
phi1 = int(phi1)
phi2 = int(phi2)

#Multiplication Logic
prod_r = r1*r2
prod_phi = phi1+phi2

#Division Logic
div_r = r1/r2
div_phi = phi1-phi2

#Output
print("The product of the given polar coordinates are ({},{})".format(prod_r,prod_phi))
print("The division of the given polar coordinates are ({},{})".format(div_r,div_phi))