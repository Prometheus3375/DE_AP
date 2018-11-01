from math import exp

InvalidY = None
C = 0.


def InitFunction(x0: float, y0: float, bad_y):
    global C, InvalidY
    InvalidY = bad_y
    try:
        C = exp(2. * x0) * (y0 + 1. - 2. * x0)
    except OverflowError:
        return "Invalid initial conditions"


def YPrime(x: float, y: float):
    try:
        return 4. * x - 2 * y
    except OverflowError:
        return InvalidY


def Y(x: float):
    try:
        return C * exp(-2. * x) + 2. * x - 1.
    except OverflowError:
        return InvalidY
