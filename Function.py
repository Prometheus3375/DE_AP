from math import cos, tan, pow, ceil, pi, atan
from Helpers import cbrt, TakeFloats


C = 0.
Trivial = False
HasAsymptotes = False
asymptotes = []


def InitFunction(xlist: list, y0: float):
    global C, Trivial, HasAsymptotes, asymptotes
    x0 = xlist[0]
    if cos(x0) == 0.:
        return None
    if y0 == 0.:
        Trivial = True
        return xlist
    C = pow(y0 * cos(x0), -3) + 3. * tan(x0)
    l = len(xlist)
    X = xlist[l - 1]
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
    # asymptotes = []
    asymptotes.extend(cosx_asym)
    asymptotes.extend(tanx_asym)
    xlist.extend(asymptotes)
    xlist.sort()
    return xlist


def IsXAsymptote(x: float):
    return x in asymptotes


def YPrime(x: float, y: float):
    if Trivial:
        return 0.
    return pow(y, 4) * cos(x) + y * tan(x)


def Y(x: float):
    if Trivial:
        return 0.
    return 1. / (cos(x) * cbrt(C - 3 * tan(x)))


def TakeAsympotesValues(ylists: tuple):
    if HasAsymptotes:
        x_asympt = []
        points = len(asymptotes)
        for x in asymptotes:
            x_asympt.append(x)
            x_asympt.append(x)
            x_asympt.append(x)
        y_max = []
        y_min = []
        L = len(ylists)
        for l in range(L):
            y_max.append(max(TakeFloats(ylists[l])))
            y_min.append(min(TakeFloats(ylists[l])))
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
