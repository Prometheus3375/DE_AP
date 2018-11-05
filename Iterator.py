from Function import Y, YPrime
from Globals import NaN as InvalidY
from typing import Callable


xlist = None
n = 0
h = 0.
x0 = 0.
y0 = 0.
X = 0.


def Init(p_x0: float, p_y0: float, p_X: float) -> None:
    global x0, y0, X
    x0 = p_x0
    y0 = p_y0
    X = p_X


def EvaluateIVP(N: int, methods: list) -> list:
    global xlist, h, n
    h = (X - x0) / N
    xlist = [x0 + h * i for i in range(N)]
    n = len(xlist)
    ylists = [[Y(xlist[i]) for i in range(n)]]
    n -= 1
    for m in methods:
        ylists.append(TakeYList(m))
    return ylists


def TakeYList(method: Callable[[float, float, float, Callable[[float, float], float]], float]) -> list:
    ylist = [y0]
    for i in range(n):
        try:
            k = method(xlist[i], ylist[i], h, YPrime)
        except OverflowError:
            k = InvalidY
        ylist.append(k)
    return ylist
