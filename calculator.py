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

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    else:
        return math.log(a, b)

def exp(a, b):
    return a ** b