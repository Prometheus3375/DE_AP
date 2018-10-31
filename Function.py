from math import exp


C = 0.
Values = []


def InitFunction(xlist: list, y0: float):
    global C, Values
    x0 = xlist[0]
    C = exp(2. * x0) * (y0 + 1. - 2 * x0)
    print(C)
    # Obtain y values
    Values = [y0] + [Y(xlist[i]) for i in range(1, len(xlist))]
    return xlist


def YPrime(x: float, y: float):
    return 4. * x - 2 * y


def Y(x: float):
    return C * exp(-2. * x) + 2. * x - 1
