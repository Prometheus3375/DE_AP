from typing import Callable
import Methods


# Error messages
Error_x0_y0_type = "x0 and y0 must be real numbers"
Error_Overflow = "Overflow"
Error_X_type = "X must be real number"
Error_X_less_than_x0 = "X must be greater than x0"
Error_OneN_type = "N must be positive integer"
Error_MultipleN_type = "Range bounds must be positive integers"
Error_MultipleN_invalid_range = "Invalid range"
# Defaults
def_x0 = str(0.)
def_y0 = str(0.)
def_X = str(3.)
def_N = str(128)
def_N0 = str(128)
def_Nk = str(384)
# Globals
ErrorTextColor = "#cc3333"
WindowTitle = "Simple Plotter"
NaN = float("nan")
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


def InitData() -> None:
    # Methods
    AddMethod("Euler", 204, 204, 51, Methods.Euler),
    AddMethod("Improved Euler", 51, 204, 51, Methods.ImprovedEuler),
    AddMethod("Runge-Kutta", 204, 51, 51, Methods.RungeKutta)


def GetAllNames() -> list:
    return AllNames


def GetAllColors() -> list:
    return AllColors


def GetMethodNames() -> list:
    return MethodNames


def GetMethodColors() -> list:
    return MethodColors


def GetMethodFuncts() -> list:
    return MethodFuncts


def GetMethodsAmount() -> int:
    return MethodsAmount
