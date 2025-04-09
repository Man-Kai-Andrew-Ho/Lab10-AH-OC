#https://github.com/Man-Kai-Andrew-Ho/Lab10-AH-OC
#Partner 1 : Andrew Ho
#Partner 2 : Oscar Cao
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""


import math

from xml.dom import VALIDATION_ERR


# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError

    return b / a

def logarithm(a, b):
    if a <= 1 or b <= 0:
        raise ValueError

    return math.log(b, a)

def exp(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError

    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

