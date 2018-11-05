from typing import Callable
import Methods


# Globals
NaN = float("nan")
OnFunctionInitError = "Invalid initial conditions"
AnalyticalName = "Analytical"
AnalyticalColor = "rgb(51, 51, 204)"
# Vars
AllNames = [AnalyticalName]
AllColors = [AnalyticalColor]
MethodNames = []
MethodColors = []
MethodFuncts = []
MethodsAmount = 0


def AddMethod(name: str, red: int, green: int, blue: int,
                 f: Callable[[float, float, float, Callable[[float, float], float]], float]) -> None:
    global MethodsAmount
    MethodNames.append(name)
    AllNames.append(name)
    color = "rgb(" + str(red) + ", " + str(green) + ", " + str(blue) + ")"
    MethodColors.append(color)
    AllColors.append(color)
    MethodFuncts.append(f)
    MethodsAmount += 1


def Init() -> None:
    # Methods
    AddMethod("Euler", 51, 51, 204, Methods.Euler),
    AddMethod("Improved Euler", 204, 204, 51, Methods.ImprovedEuler),
    AddMethod("Runge-Kutta", 204, 51, 51, Methods.RungeKutta)
