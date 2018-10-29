def Euler(xi: float, yi: float, h: float, yprime):
    return yi + h * yprime(xi, yi)


def ImprovedEuler(xi: float, yi: float, h: float, yprime):
    k1 = yprime(xi, yi)
    k2 = yprime(xi + h, yi + h * k1)
    return yi + h * (k1 + k2) / 2


def RungeKutta(xi: float, yi: float, h: float, yprime):
    k1 = yprime(xi, yi)
    xz = xi + h / 2
    k2 = yprime(xz, yi + h * k1 / 2)
    k3 = yprime(xz, yi + h * k2 / 2)
    k4 = yprime(xi + h, yi + h * k3)
    return yi + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
