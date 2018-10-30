from math import cos, tan, pow, ceil, pi, atan
from Helpers import cbrt, TakeFloats


C = 0.
Trivial = False
HasAsymptotes = False
Asymptotes = []
Values = []


def InitFunction(xlist: list, y0: float, BadYSign):
    global C, Trivial, HasAsymptotes, Asymptotes, Values
    x0 = xlist[0]
    if cos(x0) == 0.:
        print("Bad x0!")
        return None
    if y0 == 0.:
        Trivial = True
        Values = [0.] * (len(xlist))
        return xlist
    C = pow(y0 * cos(x0), -3) + 3. * tan(x0)
    X = xlist[len(xlist) - 1]
    HasAsymptotes = True
    # Evaluate asymptotes:
    # cos(x) = 0
    k1 = ceil(x0 / pi - 0.5)
    k2 = ceil(X / pi - 0.5)
    cosx_asym = [pi * (0.5 + k) for k in range(k1, k2)]
    # C - 3tan(x) = 0
    v = atan(C / 3)
    k1 = ceil((x0 - v) / pi)
    k2 = ceil((X - v) / pi)
    tanx_asym = [v + pi * k for k in range(k1, k2)]
    # Append found values to asymptotes and xlist
    Asymptotes.extend(cosx_asym)
    Asymptotes.extend(tanx_asym)
    xlist.extend(Asymptotes)
    # Remove duplicates and sort
    xlist = list(set(xlist))
    xlist.sort()
    # Obtain y values
    Values = [y0]
    for i in range(1, len(xlist)):
        if IsXAsymptote(xlist[i]):
            Values.append(BadYSign)
        else:
            Values.append(Y(xlist[i]))
    return xlist


def IsXAsymptote(x: float):
    return x in Asymptotes


def YPrime(x: float, y: float):
    return pow(y, 4) * cos(x) + y * tan(x)


def Y(x: float):
    if Trivial:
        return 0.
    return 1. / (cos(x) * cbrt(C - 3 * tan(x)))


def TakeAsympotesToPlot(ylists: tuple):
    # Move this function to Plotter!!!
    if HasAsymptotes:
        # Init x values to plot
        x_asympt = []
        points = len(Asymptotes)
        for x in Asymptotes:
            x_asympt.append(x)
            x_asympt.append(x)
            x_asympt.append(x)
        # Determine max and min y values for every graph
        y_max = []
        y_min = []
        L = len(ylists)
        for l in range(L):
            y_max.append(max(TakeFloats(ylists[l])) + 1)
            y_min.append(min(TakeFloats(ylists[l])) - 1)
        # Init y values to plot
        y_asympt = []
        for l in range(L):
            temp = []
            for i in range(points):
                temp.append(y_min[l])
                temp.append(y_max[l])
                temp.append(None)
            y_asympt.append(temp)
        return x_asympt, y_asympt
    return None, None
