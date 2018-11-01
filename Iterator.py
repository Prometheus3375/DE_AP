from Function import Y, YPrime


xlist = None
n = 0
h = 0.
x0 = 0.
y0 = 0.
X = 0.
InvalidY = None


def Init(p_x0: float, p_y0: float, p_X: float, bad_y):
    global x0, y0, X, InvalidY
    x0 = p_x0
    y0 = p_y0
    X = p_X
    InvalidY = bad_y


def EvaluateIVP(N: int, methods: tuple):
    global xlist, h, n
    h = (X - x0) / N
    xlist = [x0 + h * i for i in range(N)]
    n = len(xlist)
    ylists = [[Y(xlist[i]) for i in range(n)]]
    n -= 1
    for m in methods:
        ylists.append(TakeYList(m))
    return ylists


def TakeYList(method):
    ylist = [y0]
    for i in range(n):
        try:
            k = method(xlist[i], ylist[i], h, YPrime)
        except OverflowError:
            k = InvalidY
        ylist.append(k)
    return ylist
