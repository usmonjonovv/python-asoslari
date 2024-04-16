# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:43:33 2024

@author: usmonjonov.k
"""
#1-mashq
def age_calcuator(name = input("Your name:"),current_year = 2024):
    """Function to calculate the age of user"""
    print(f"Name:{name.title()}")
    print(f"Age:{current_year-born_year}")
born_year = input("When were you born?\n- ") 
born_year = int(born_year)
print(age_calcuator())
#2-mashq
def square_cube(number=input('You can enter any number you want!\n-')   ):
    """function that calculate square and cube of numbers"""
    number = int(number)
    print(f"Square of number is: {number**2}")
    print(f"Cube of number is: {number**3}")
print(square_cube())
#3-mashq
def a_number(number = input("Enter any number you want:")):
    """Number analyzer"""
    number = int(number)
    if number%2==0:
        print(f"{number} is even number.")
    else:
        print(f"{number} is odd number.")
print(a_number())
#4-mashq
def c_numbers(number1 = input("Type any number you want:"),number2 = input("Type second number you want:")):
    number1 = int(number1)
    number2 = int(number2)
    if number1 > number2:
        print(f"{number1} is bigger than {number2}")
    elif number1 < number2:
        print(f"{number1} is smaller than {number2}")
    else:
        print(f"{number1} is equal to {number2}")
print(c_numbers())
#5-mashq
def x_y(x=input("Type any number you want:"),y=input("Type second number you want:")):
    """Function that calculate x**y"""
    x = int(x)
    y = int(y)
    print(x**y)
print(x_y())
#6-mashq
def x_y(x=input("Type any number you want:"),y=2):
    """Function that calculate square of numbers"""
    x = int(x)
    print(x**y)
print(x_y())
#7-mashq
def one_ten(number = input("Type any number:")):
    """Function to know whether number can be divided to numbers from 1 to 10"""
    number = int(number)
    for n in range(1,11):
        if number%n==0:
            print(f"{number} can be divided to {n} without residual.")
print(one_ten())