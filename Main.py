import Iterator
from Plotter import Plot
from Function import InitFunction
import Methods


NaN = float("nan")
methods = (Methods.Euler, Methods.ImprovedEuler, Methods.RungeKutta)
MethodsAmount = len(methods)
all_names = ("Analytical", "Euler", "Improved Euler", "Runge-Kutta")
m_names = all_names[1:]
all_colors = ("rgb(51, 51, 204)", "rgb(204, 204, 51)", "rgb(51, 204, 51)", "rgb(204, 51, 51)")
m_colors = all_colors[1:]
Analytical = None


def CalculateErrors(m: list):
    return [abs(Analytical[i] - m[i]) for i in range(l)]


PlotValuesOnX = True
PlotErrorsOnX = True
x0 = 0.
y0 = 0.0001
X = x0 + 3.
# N = [i for i in range(192, 384)]
N = [384]
GridCellsAmount = len(N)
SingleN = GridCellsAmount == 1
if X <= x0:
    print("Bad X!")
    exit(0)
x0s = str(x0)
signature = "IVP y(" + x0s + ") = " + str(y0) + " on [" + x0s + ", " + str(X) + "]"
# Sending IVP to function
# If initial conditions are appropriate, proceed further
# Else throw an error with taken message
message = InitFunction(x0, y0, NaN)
if not (message is None):
    print(message)
    exit(0)
Iterator.Init(x0, y0, X, NaN)
MaxErrors = []
for ni in N:
    nis = signature + " with " + str(ni) + " steps amount"
    y_lists = Iterator.EvaluateIVP(ni, methods)
    xlist = Iterator.xlist
    Analytical = y_lists[0]
    computed = y_lists[1:]
    l = len(xlist)
    Plot(xlist, y_lists, all_names, all_colors, nis, "X Axis", "Y Axis", SingleN)
    errors = [CalculateErrors(computed[i]) for i in range(MethodsAmount)]
    MaxErrors.append([max(errors[i]) for i in range(MethodsAmount)])
    plotname = "Dependence of global truncation error for " + nis
    # Plot(xlist, errors, m_names, m_colors, plotname, "X Axis", "Global Truncation Error", SingleN)

MaxErrors = list(map(list, zip(*MaxErrors)))  # Transposes MaxErrors matrix
plotname = "Dependence of maximum global truncation error from number of grid cells for " + signature
# Plot(N, MaxErrors, m_names, m_colors, plotname, "Number of Grid Cells", "Maximum Global Truncation Error", True)
