#https://github.com/dmertis/lab10-DD-FM
#Partner 1: Demetri Delerme
#Partner 2: Frank Maronas

import math
def square_root(a):
    b = math.sqrt(a)
    if a < 0:
        raise ValueError
    else:
        return b

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def logarithm(a, b):
    if a <= 0 or b <= 1:
        raise ValueError
    else:
        return math.log(a, b)

def exp(a, b):
    return a ** b