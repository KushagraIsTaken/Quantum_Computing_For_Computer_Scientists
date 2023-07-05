#Take the program that you wrote in the last programming drill and make it also perform subtraction and division of complex numbers. In addition, let the user enter a complex number and have the computer return its modulus and conjugate

import os
import math
os.system('cls')
print("This Program performs two tasks.")
print("Enter 1 if you want to enter a complex number and find its conjugate, and modulus")
print("Enter 2 if you want to do math on two complex numbers")
x = input("Please Enter your choice : ")

if(int(x)==2) :
    print("This Program does the math of two complex numbers")
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

    #Subtraction Logic

    a_diff_new = a1-a2
    b_diff_new = b1-b2

    #Multiplication Logic

    a_prod_new = (a1*a2)-(b1*b2)
    b_prod_new = (a1*b2)+(a2*b1)

    #Division Logic

    a_div_new = ((a1*a2)+(b1*b2))/a1**2+b1**2
    b_div_new = ((a2*b1)-(a1*b2))/a1**2+b1**2

    #Result Output

    print("The sum of both complex numbers is {} + {}i".format(a_sum_new,b_sum_new))
    print("The product of both complex numbers is {} + {}i ".format(a_prod_new,b_prod_new))
    print("The difference of both complex numbers is {} + {}i".format(a_diff_new,b_diff_new))
    print("The division of both complex numbers is {} + {}i ".format(a_div_new,b_div_new))  
elif(int(x)==1):
    print("This Program finds the conjugate and modulus complex numbers")
    print("A complex number a+ib can be input as a,b")
    a,b = input("Input the complex number : ").split(",")

    a = int(a)
    b = int(b)

    conj_a = a
    conj_b = -b

    mod = math.sqrt(a**2+b**2)

    #Result Output
    print("The conjugate of the complex numbers is {} + {}i".format(conj_a,conj_b))
    print("Modulus of the complex number is", mod)
