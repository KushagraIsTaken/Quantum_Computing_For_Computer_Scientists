# Programming Drill 1.1.1 Write a program that accepts two complex numbers and outputs their sum and their product

import os
os.system('cls')
print("This Program computes the sum and product of two complex numbers")
print("A complex number a+ib can be input as a,b")
a1,b1 = input("Enter the First Complex Number : ").split(",") #Input First Complex Number
a2,b2 = input("Enter the Second Complex Number : ").split(",") #Input Second Complex Number

#Type Casting 

a1 = int(a1)
a2 = int(a2)
b1 = int(b1)
b2 = int(b2)

#Addition Logic

a_sum_new = a1+a2
b_sum_new = b1+b2

#Multiplication Logic

a_prod_new = (a1*a2)-(b1*b2)
b_prod_new = (a1*b2)+(a2*b1)

#Result Output

print("The sum of both complex numbers is {} + {}i".format(a_sum_new,b_sum_new))
print("The product of both complex numbers is {} + {}i ".format(a_prod_new,b_prod_new)) 