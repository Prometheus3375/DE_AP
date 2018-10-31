from math import ceil
from Plotter import Plot
import Function as Funct
import Methods


def TakeYList(method):
    ylist = [y0]
    for i in range(n):
        if ylist[i] is BadYSign:
            k = ylist_Analytical[i + 1]
        else:
            try:
                k = method(xlist[i], ylist[i], h, YPrime)
            except OverflowError:
                k = BadYSign
        ylist.append(k)
    return ylist


x0 = 0.
y0 = 0.
X = 3.
# Constants
BadYSign = float("nan")
if X < x0:
    print("Bad X!")
    exit(0)
# Determine range and amount
h = 1. / 128.
n = ceil((X - x0) / h)
# n = 19
# h = (X - x0) / n
# Init Function
xlist = Funct.InitFunction([x0 + h * i for i in range(n)], y0)
if xlist is None:
    exit(0)
n = len(xlist) - 1
YPrime = Funct.YPrime
x0s = str(x0)
signature = "plot for the IVP y(" + x0s + ") = " + str(y0) + \
            " on [" + x0s + ", " + str(X) + "] with step range " + str(h)
# Compute sets of y for every method
ylist_Analytical = Funct.Values
ylist_Euler = TakeYList(Methods.Euler)
ylist_ImpEuler = TakeYList(Methods.ImprovedEuler)
ylist_RungeKutta = TakeYList(Methods.RungeKutta)
y_lists = (ylist_Analytical, ylist_Euler, ylist_ImpEuler, ylist_RungeKutta)
names = ("Analytical", "Euler", "Improved Euler", "Runge-Kutta")
colors = ("rgb(51, 51, 204)", "rgb(204, 204, 51)", "rgb(51, 204, 51)", "rgb(204, 51, 51)")
plotname = "Function " + signature
Plot(xlist, y_lists, names, colors, plotname)
