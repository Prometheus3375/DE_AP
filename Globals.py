from typing import Callable
import Methods


# Defaults
def_x0 = str(0.)
def_y0 = str(0.)
def_X = str(3.)
def_N = str(128)
def_N0 = str(128)
def_Nk = str(384)
# Globals
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
