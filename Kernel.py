from Plotter import Plot
from typing import Callable
from Function import Y, YPrime
from Globals import GetAllColors, GetAllNames, GetMethodsAmount, GetMethodColors, GetMethodFuncts, GetMethodNames, NaN


def CalculateErrors(a: list, m: list, l: int) -> list:
    return [abs(a[i] - m[i]) for i in range(l)]


def ProceedMethod(xlist: list, y0: float, points: int, step: float,
                  method: Callable[[float, float, float, Callable[[float, float], float]], float]) -> list:
    ylist = [y0]
    for i in range(points):
        try:
            k = method(xlist[i], ylist[i], step, YPrime)
        except OverflowError:
            k = NaN
        ylist.append(k)
    return ylist


def Execute(x0: float, y0: float, X: float, N0: int, Nk: int,
            PlotValues: bool, ValuesAutoOpen: bool,
            PlotErrors: bool, ErrorsAutoOpen: bool,
            PlotDependence: bool, DependenceAutoOpen: bool) -> None:
    N = [n for n in range(N0, Nk + 1)]
    x0s = str(x0)
    signature = "IVP y(" + x0s + ") = " + str(y0) + " on [" + x0s + ", " + str(X) + "]"
    MaxErrors = []
    for ni in N:
        nis = signature + " with " + str(ni) + " steps"
        # Take xlist and analytical solution
        h = (X - x0) / ni
        xlist = [x0 + h * i for i in range(ni)]
        l = len(xlist)
        analytical = [Y(xlist[i]) for i in range(l)]
        ylists = [analytical]
        # Compute numerical methods
        l -= 1  # because numerical methods does not need last x
        for m in GetMethodFuncts():
            ylists.append(ProceedMethod(xlist, y0, l, h, m))
        computed = ylists[1:]
        l += 1
        # Plot values if necessary
        if PlotValues:
            Plot(xlist, ylists, GetAllNames(), GetAllColors(), nis, "X Axis", "Y Axis", ValuesAutoOpen)
        # Compute and plot errors if necessary
        if PlotErrors or PlotDependence:
            errors = [CalculateErrors(analytical, computed[i], l) for i in range(GetMethodsAmount())]
            MaxErrors.append([max(errors[i]) for i in range(GetMethodsAmount())])
            if PlotErrors:
                plotname = "Dependence of absolute global truncation error for " + nis
                Plot(xlist, errors, GetMethodNames(), GetMethodColors(), plotname, "X Axis",
                     "Absolute Global Truncation Error", ErrorsAutoOpen)
    if PlotDependence:
        MaxErrors = list(map(list, zip(*MaxErrors)))  # Transposes MaxErrors matrix
        plotname = "Dependence of maximum absolute global truncation error from number of grid cells for " + signature
        Plot(N, MaxErrors, GetMethodNames(), GetMethodColors(), plotname, "Number of Grid Cells",
             "Maximum Absolute Global Truncation Error", DependenceAutoOpen)
