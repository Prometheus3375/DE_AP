from math import exp
from Globals import NaN as InvalidY


C = 0.


def InitFunction(x0: float, y0: float) -> bool:
    global C
    try:
        C = exp(2. * x0) * (y0 + 1. - 2. * x0)
        return False
    except OverflowError:
        return True


def YPrime(x: float, y: float) -> float:
    try:
        return 4. * x - 2. * y
    except OverflowError:
        return InvalidY


def Y(x: float) -> float:
    try:
        return C * exp(-2. * x) + 2. * x - 1.
    except OverflowError:
        return InvalidY
