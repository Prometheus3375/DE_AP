from InterfaceClasses import *
from Globals import def_N, def_N0, def_Nk, def_X, def_x0, def_y0, WindowTitle,\
    Error_Overflow, Error_MultipleN_invalid_range, Error_OneN_type, Error_X_less_than_x0, Error_x0_y0_type,\
    Error_MultipleN_type, Error_X_type, ErrorTextColor
from Function import InitFunction
from Extencions import isfloat
from Kernel import Execute


# Flags
DefaultOneNValue = True
DefaultMultipleNValue = not DefaultOneNValue
# OneN flags
DefaultOneN_PlotValues_AutoOpen = True
DefaultOneN_PlotErrors = False
DefaultOneN_PlotErrors_AutoOpen = True
# MultipleN flags
DefaultMultipleN_PlotDependence_AutoOpen = True
DefaultMultipleN_PlotValues = False
DefaultMultipleN_PlotErrors = False
# Button
ButtonText = "Plot"
ButtonWidth = 8
ButtonHeight = 2


# Root
root = Tk()
# Vars
OneNVar = BooleanVar()
# OneN vars
OneN_PlotValues_AutoOpenVar = BooleanVar()
OneN_PlotErrorsVar = BooleanVar()
OneN_PlotErrors_AutoOpenVar = BooleanVar()
# MultipleN vars
MultipleN_PlotDependence_AutoOpenVar = BooleanVar()
MultipleN_PlotValuesVar = BooleanVar()
MultipleN_PlotErrorsVar = BooleanVar()


def InitVars() -> None:
    OneNVar.set(DefaultOneNValue)

    OneN_PlotValues_AutoOpenVar.set(DefaultOneN_PlotValues_AutoOpen)
    OneN_PlotErrorsVar.set(DefaultOneN_PlotErrors)
    OneN_PlotErrors_AutoOpenVar.set(DefaultOneN_PlotErrors_AutoOpen)

    MultipleN_PlotDependence_AutoOpenVar.set(DefaultMultipleN_PlotDependence_AutoOpen)
    MultipleN_PlotValuesVar.set(DefaultMultipleN_PlotValues)
    MultipleN_PlotErrorsVar.set(DefaultMultipleN_PlotErrors)


def InitWindowContents() -> None:
    global x0, y0, ivp_err, X, X_err, OneN, OneN_err, N0, Nk, MultipleN_err, OneNFrame, MultipleNFrame,\
        ErrorsAutoOpen
    # Initial Conditions
    InitCond = FrameExt(MainWindowOffset, MainWindowOffset, text="Initial conditions")
    nextw = InitCond.AddPoint("x0:", RealEntryWidth, def_x0)
    x0 = nextw.entry
    nextw = InitCond.AddPoint("y0:", RealEntryWidth, def_y0, x=nextw.GetWidth() + XSpaceBetweenPx)
    y0 = nextw.entry
    nextw = InitCond.AddLabel(text=Error_x0_y0_type, fg=ErrorTextColor, y=nextw.endy + 1)
    ivp_err = nextw.label
    nextw = InitCond.AddPoint("X:", RealEntryWidth, def_X, y=nextw.endy + YSpaceBetweenPx + 1)
    X = nextw.entry
    nextw = InitCond.AddLabel(text=Error_X_less_than_x0, fg=ErrorTextColor, y=nextw.endy + 1)
    X_err = nextw.label
    InitCond.ResizeXSimple()
    InitCond.ResizeYSimple()
    # Steps
    Steps = LabelExt(MainWindowOffset, InitCond.endy + MainWindowOffset, text="Amount of steps")
    # One step
    OneNFrame = FrameExt(Steps.x, Steps.endy,
                         labelwidget=Radiobutton(text="Single value",
                                            variable=OneNVar,
                                            value=DefaultOneNValue,
                                            command=ToggleStepAmountMode),
                         enable=DefaultOneNValue)
    nextw = OneNFrame.AddPoint("N:", IntEntryWidth, def_N)
    OneN = nextw.entry
    nextw = OneNFrame.AddLabel(text=Error_OneN_type, fg=ErrorTextColor, y=nextw.endy + 1)
    OneN_err = nextw.label
    nextw = OneNFrame.AddStaticRadioButton("Plot of function", y=nextw.endy + 1)
    nextw = OneNFrame.AddCheckButton("Auto-open plot", OneN_PlotValues_AutoOpenVar,
                                     x=OneNFrame.xint + BoxWidth, y=nextw.endy + 1)
    nextw = OneNFrame.AddCheckButton("Plot of absolute errors", OneN_PlotErrorsVar,
                                     y=nextw.endy + 1,
                                     command=ToggleErrorAutoOpen)
    ErrorsAutoOpen = OneNFrame.AddCheckButton("Auto-open plot", OneN_PlotErrors_AutoOpenVar,
                                              parent=nextw)
    # Resize OneN_Frame
    OneNFrame.ResizeXSimple()

    # Several steps
    MultipleNFrame = FrameExt(OneNFrame.endx - OneNFrame.offx + 1, Steps.endy,
                              labelwidget=Radiobutton(text="Range of values",
                                                 variable=OneNVar,
                                                 value=DefaultMultipleNValue,
                                                 command=ToggleStepAmountMode),
                              enable=DefaultMultipleNValue)
    nextw = MultipleNFrame.AddPoint("From", IntEntryWidth, def_N0)
    N0 = nextw.entry
    nextw = MultipleNFrame.AddPoint(" to", IntEntryWidth, def_Nk, x=nextw.endx + 1)
    Nk = nextw.entry
    nextw = MultipleNFrame.AddLabel(text=Error_MultipleN_type, fg=ErrorTextColor, y=nextw.endy + 1)
    MultipleN_err = nextw.label
    nextw = MultipleNFrame.AddStaticRadioButton("Plot of absolute error dependence", y=nextw.endy + 1)
    nextw = MultipleNFrame.AddCheckButton("Auto-open plot", MultipleN_PlotDependence_AutoOpenVar,
                                          x=MultipleNFrame.xint + BoxWidth,
                                          y=nextw.endy + 1)
    nextw = MultipleNFrame.AddCheckButton("Plots of function for every N", MultipleN_PlotValuesVar,
                                          y=nextw.endy + 1)
    MultipleNFrame.AddCheckButton("Plots of absolute errors for every N", MultipleN_PlotErrorsVar, y=nextw.endy + 1)
    # Resize MultipleN_Frame
    MultipleNFrame.ResizeXSimple()

    # Set width and height
    maxy = max(max([w.endy for w in OneNFrame.widgets]),
               max([w.endy for w in MultipleNFrame.widgets]))
    OneNFrame.ResizeY(maxy)
    MultipleNFrame.ResizeY(maxy)
    # Make button
    SimpleButton(InitCond.endx + XSpaceBetweenPx * 5, InitCond.y + InitCond.GetHeight() // 2,
                 ButtonText, ButtonWidth, ButtonHeight, Check)


def InitInterface() -> None:
    InitVars()
    InitWindowContents()
    root.title(WindowTitle)
    root.geometry(str(MainWindowOffset + max(w.endx for w in AllFrames))
                  + "x"
                  + str(MainWindowOffset + max(w.endy for w in AllFrames)))
    root.resizable(False, False)
    # Flush error texts
    ivp_err.config(text="")
    X_err.config(text="")
    OneN_err.config(text="")
    MultipleN_err.config(text="")
    root.mainloop()


def ToggleStepAmountMode() -> None:
    mode = OneNVar.get()
    OneNFrame.Switch(mode)
    MultipleNFrame.Switch(not mode)
    OneN_err.config(text="")
    MultipleN_err.config(text="")


def ToggleErrorAutoOpen() -> None:
    mode = OneN_PlotErrors_AutoOpenVar.get()
    ErrorsAutoOpen.Switch(mode)


def Check() -> None:
    # Check x0 and y0
    x0s = str(x0.get())
    y0s = str(y0.get())
    if not (isfloat(x0s) and isfloat(y0s)):
        ivp_err.config(text=Error_x0_y0_type)
        return
    ivp_err.config(text="")
    x0v = float(x0s)
    y0v = float(y0s)
    # Check X
    Xs = str(X.get())
    if not isfloat(Xs):
        X_err.config(text=Error_X_type)
        return
    Xv = float(Xs)
    if x0v >= Xv:
        X_err.config(text=Error_X_less_than_x0)
        return
    X_err.config(text="")
    # Check N
    mode = OneNVar.get()
    if mode:
        N0s = str(OneN.get())
        if not N0s.isdecimal():
            OneN_err.config(text=Error_OneN_type)
            return
        N0v = int(N0s)
        Nkv = N0v
        if N0v <= 0:
            OneN_err.config(text=Error_OneN_type)
            return
    else:
        N0s = str(N0.get())
        Nks = str(Nk.get())
        if not (N0s.isdecimal() and Nks.isdecimal()):
            MultipleN_err.config(text=Error_MultipleN_type)
            return
        N0v = int(N0s)
        Nkv = int(Nks)
        if not (N0v > 0 and Nkv > 0):
            MultipleN_err.config(text=Error_MultipleN_type)
            return
        if N0v >= Nkv:
            MultipleN_err.config(text=Error_MultipleN_invalid_range)
            return
    OneN_err.config(text="")
    MultipleN_err.config(text="")
    if InitFunction(x0v, y0v):
        ivp_err.config(text=Error_Overflow)
        return
    Execute(x0v, y0v, Xv, N0v, Nkv,
            mode or MultipleN_PlotValuesVar.get(), mode and OneN_PlotValues_AutoOpenVar.get(),
            (mode and OneN_PlotErrorsVar.get()) or ((not mode) and MultipleN_PlotErrorsVar.get()),
            mode and OneN_PlotErrors_AutoOpenVar.get(),
            not mode, MultipleN_PlotDependence_AutoOpenVar.get())
