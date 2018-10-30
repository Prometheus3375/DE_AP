from math import ceil
from Plotter import Plot
import Function as Funct
import Methods


def TakeYList(method):
    ylist = [y0]
    for i in range(n - 1):
        if Funct.IsXAsymptote(xlist[i]):
            k = BadYSign
        elif method == Analytical:
            try:
                k = Analytical(xlist[i])
            except OverflowError:
                k = BadYSign
        elif ylist[i] is BadYSign:
            k = BadYSign
        else:
            try:
                k = method(xlist[i], ylist[i], h, YPrime)
            except OverflowError:
                k = BadYSign
        ylist.append(k)
    return ylist


x0 = 0.
y0 = 1.
X = 9.5
UseRange = True
PlotAsymptotes = True
if X < x0:
    print("Bad X!")
    exit(0)
# Determine range and amount
if UseRange:
    h = 1. / 128.
    n = ceil((X - x0) / h)
else:
    n = 19
    h = (X - x0) / n
# Init Function
xlist = Funct.InitFunction([x0 + h * i for i in range(n)], y0)
if xlist is None:
    print("Bad x0!")
    exit(0)
BadXSign = None
BadYSign = None
Analytical = Funct.Y
YPrime = Funct.YPrime
x0s = str(x0)
signature = "plot for the IVP y(" + x0s + ") = " + str(y0) + \
            " on [" + x0s + ", " + str(X) + "] with step range " + str(h)
# Compute sets of y for every method
ylist_Analytical = TakeYList(Analytical)
ylist_Euler = TakeYList(Methods.Euler)
ylist_ImpEuler = TakeYList(Methods.ImprovedEuler)
ylist_RungeKutta = TakeYList(Methods.RungeKutta)
# Init data to plot
y_lists = (ylist_Analytical, ylist_Euler, ylist_ImpEuler, ylist_RungeKutta)
names = ("Analytical", "Euler", "Improved Euler", "Runge-Kutta")
colors = ("rgb(51, 51, 204)", "rgb(204, 204, 51)", "rgb(51, 204, 51)", "rgb(204, 51, 51)")
plotname = "Function " + signature
if PlotAsymptotes:
    l = Funct.TakeAsympotesToPlot(y_lists)
    x_asympt = l[0]
    y_asympt = l[1]
    Plot(xlist, y_lists, names, colors, plotname, x_asympt, y_asympt)
else:
    Plot(xlist, y_lists, names, colors, plotname)
