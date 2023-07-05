#Write a program that converts a complex number from its Cartesian representation to its polar representation and vice versa.

import os
import math

os.system('cls')
print("Enter 1 if you want to convert cartesian coordinates to polar coordinates")
print("Enter 2 if you want to convert polar coordinates to cartesian coordinates")
select = input("Please Enter your choice : ")

if (int (select)==1) :
    x,y = input("Enter Cartesian coordinates in the form a,b : ").split(",")
    x = int(x)
    y = int(y)
    p_mod = math.sqrt(x**2+y**2)
    phi = math.atan(x/y)
    #Output

    print("Polar Coordinates are ({}, {})".format(p_mod,phi))
elif (int(select)==2) :
    p,theta = input("Enter Polar coordinates in the form p,phi : ").split(",")
    p = int(p)
    theta = int(theta)
    x = p*math.cos(theta)
    y = p*math.sin(theta)
    #Output

    print("Cartsian Coordinates are ({}, {})".format(x,y))


