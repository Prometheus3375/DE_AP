import Iterator
from Plotter import Plot
from Function import InitFunction
import Globals


def CalculateErrors(a: list, m: list, l: int) -> list:
    return [abs(a[i] - m[i]) for i in range(l)]


def Main(x0: float, y0: float, X: float, N0: int, Nk: int) -> None:
    X += x0 + 3.
    N = tuple(n for n in range(N0, Nk + 1))
    GridCellsAmount = len(N)
    SingleN = GridCellsAmount == 1
    x0s = str(x0)
    signature = "IVP y(" + x0s + ") = " + str(y0) + " on [" + x0s + ", " + str(X) + "]"
    # Sending IVP to function
    # If initial conditions are appropriate, proceed further
    # Else throw an error
    if InitFunction(x0, y0):
        print(Globals.OnFunctionInitError)
        exit(0)
    Iterator.Init(x0, y0, X)
    MaxErrors = []
    for ni in N:
        nis = signature + " with " + str(ni) + " steps amount"
        y_lists = Iterator.EvaluateIVP(ni, Globals.MethodFuncts)
        xlist = Iterator.xlist
        Analytical = y_lists[0]
        computed = y_lists[1:]
        l = len(xlist)
        Plot(xlist, y_lists, Globals.AllNames, Globals.AllColors, nis, "X Axis", "Y Axis", SingleN)
        errors = [CalculateErrors(Analytical, computed[i], l) for i in range(Globals.MethodsAmount)]
        MaxErrors.append([max(errors[i]) for i in range(Globals.MethodsAmount)])
        plotname = "Dependence of global truncation error for " + nis
        # Plot(xlist, errors, m_names, m_colors, plotname, "X Axis", "Global Truncation Error", SingleN)

    MaxErrors = list(map(list, zip(*MaxErrors)))  # Transposes MaxErrors matrix
    plotname = "Dependence of maximum global truncation error from number of grid cells for " + signature
    # Plot(N, MaxErrors, m_names, m_colors, plotname, "Number of Grid Cells", "Maximum Global Truncation Error", True)
