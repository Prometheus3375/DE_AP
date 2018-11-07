from InterfaceClasses import *
from Globals import def_N, def_N0, def_Nk, def_X, def_x0, def_y0
from Function import InitFunction
from Extencions import isfloat
from Kernel import Execute


# Error messages
Error_x0_y0_type = "x0 and y0 must be real numbers"
Error_Overflow = "Overflow error"
Error_X_type = "X must be a real number"
Error_X_less_than_x0 = "X must be greater than x0"
Error_OneN_type = "N must be a positive integer"
Error_MultipleN_type = "Range bounds must be positive integers"
Error_MultipleN_invalid_range = "Invalid range"
# Labels
ErrorTextColor = "#cc3333"
WindowTitle = "Simple Plotter"
# Initial conditions
Text_Frame_IVP = "Initial conditions"
Text_x0 = "x0:"
Text_y0 = "y0:"
Text_X = " X:"
# Number of steps
Text_NoS = "Number of steps"
# OneN
Text_Frame_OneN = "Single value"
Text_N = "N:"
Text_AutoOpen = "Auto-open plot"
Text_PlotValues = "Plot of function"
Text_PlotErrors = "Plot of absolute errors"
# MultipleM
Text_Frame_MultipleN = "Range of values"
Text_N0 = "From"
Text_Nk = " to"
Text_PlotDependence = "Plot of absolute errors dependence"
Text_PlotValuesForN = "Plots of function for every N"
Text_PlotErrorsForN = "Plots of absolute errors for every N"

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
    global Entry_x0, Entry_y0, Label_IVP_Error, Entry_X, Label_X_Error,\
        Entry_N, Label_N_Error, Entry_N0, Entry_Nk, Label_Range_Error,\
        Frame_OneN, Frame_MultipleN, CheckButton_OneN_ErrorsAutoOpen
    # Initial Conditions
    InitCond = FrameExt(MainWindowOffset, MainWindowOffset, text=Text_Frame_IVP)
    nextw = InitCond.AddPoint(Text_x0, RealEntryWidth, def_x0)
    Entry_x0 = nextw.entry
    nextw = InitCond.AddPoint(Text_y0, RealEntryWidth, def_y0, x=nextw.GetWidth() + XSpaceBetweenPx)
    Entry_y0 = nextw.entry
    nextw = InitCond.AddLabel(text=Error_x0_y0_type, fg=ErrorTextColor, y=nextw.endy + 1)
    Label_IVP_Error = nextw.label
    nextw = InitCond.AddPoint(Text_X, RealEntryWidth, def_X, y=nextw.endy + YSpaceBetweenPx + 1)
    Entry_X = nextw.entry
    nextw = InitCond.AddLabel(text=Error_X_less_than_x0, fg=ErrorTextColor, y=nextw.endy + 1)
    Label_X_Error = nextw.label
    InitCond.ResizeXSimple()
    InitCond.ResizeYSimple()
    # Steps
    steps = LabelExt(MainWindowOffset, InitCond.endy + MainWindowOffset, text=Text_NoS)
    # One step
    Frame_OneN = FrameExt(steps.x, steps.endy,
                          labelwidget=Radiobutton(text=Text_Frame_OneN,
                                                  variable=OneNVar,
                                                  value=DefaultOneNValue,
                                                  command=ToggleStepAmountMode),
                          enable=DefaultOneNValue)
    nextw = Frame_OneN.AddPoint(Text_N, IntEntryWidth, def_N)
    Entry_N = nextw.entry
    nextw = Frame_OneN.AddLabel(text=Error_OneN_type, fg=ErrorTextColor, y=nextw.endy + 1)
    Label_N_Error = nextw.label
    nextw = Frame_OneN.AddStaticRadioButton(Text_PlotValues, y=nextw.endy + 1)
    nextw = Frame_OneN.AddCheckButton(Text_AutoOpen, OneN_PlotValues_AutoOpenVar,
                                      x=Frame_OneN.xint + BoxWidth, y=nextw.endy + 1)
    nextw = Frame_OneN.AddCheckButton(Text_PlotErrors, OneN_PlotErrorsVar,
                                      y=nextw.endy + 1,
                                      command=ToggleErrorAutoOpen)
    CheckButton_OneN_ErrorsAutoOpen = Frame_OneN.AddCheckButton(Text_AutoOpen, OneN_PlotErrors_AutoOpenVar,
                                                                parent=nextw)
    # Resize OneN_Frame
    Frame_OneN.ResizeXSimple()

    # Several steps
    Frame_MultipleN = FrameExt(Frame_OneN.endx - Frame_OneN.offx + 1, steps.endy,
                               labelwidget=Radiobutton(text=Text_Frame_MultipleN,
                                                       variable=OneNVar,
                                                       value=DefaultMultipleNValue,
                                                       command=ToggleStepAmountMode),
                               enable=DefaultMultipleNValue)
    nextw = Frame_MultipleN.AddPoint(Text_N0, IntEntryWidth, def_N0)
    Entry_N0 = nextw.entry
    nextw = Frame_MultipleN.AddPoint(Text_Nk, IntEntryWidth, def_Nk, x=nextw.endx + 1)
    Entry_Nk = nextw.entry
    nextw = Frame_MultipleN.AddLabel(text=Error_MultipleN_type, fg=ErrorTextColor, y=nextw.endy + 1)
    Label_Range_Error = nextw.label
    nextw = Frame_MultipleN.AddStaticRadioButton(Text_PlotDependence, y=nextw.endy + 1)
    nextw = Frame_MultipleN.AddCheckButton(Text_AutoOpen, MultipleN_PlotDependence_AutoOpenVar,
                                           x=Frame_MultipleN.xint + BoxWidth,
                                           y=nextw.endy + 1)
    nextw = Frame_MultipleN.AddCheckButton(Text_PlotValuesForN, MultipleN_PlotValuesVar,
                                           y=nextw.endy + 1)
    Frame_MultipleN.AddCheckButton(Text_PlotErrorsForN, MultipleN_PlotErrorsVar, y=nextw.endy + 1)
    # Resize MultipleN_Frame
    Frame_MultipleN.ResizeXSimple()

    # Set width and height
    maxy = max(max([w.endy for w in Frame_OneN.widgets]),
               max([w.endy for w in Frame_MultipleN.widgets]))
    Frame_OneN.ResizeY(maxy)
    Frame_MultipleN.ResizeY(maxy)
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
    Label_IVP_Error.config(text="")
    Label_X_Error.config(text="")
    Label_N_Error.config(text="")
    Label_Range_Error.config(text="")
    root.mainloop()


def ToggleStepAmountMode() -> None:
    mode = OneNVar.get()
    Frame_OneN.Switch(mode)
    Frame_MultipleN.Switch(not mode)
    Label_N_Error.config(text="")
    Label_Range_Error.config(text="")


def ToggleErrorAutoOpen() -> None:
    mode = OneN_PlotErrorsVar.get()
    CheckButton_OneN_ErrorsAutoOpen.Switch(mode)


def Check() -> None:
    # Check x0 and y0
    x0s = str(Entry_x0.get())
    y0s = str(Entry_y0.get())
    if not (isfloat(x0s) and isfloat(y0s)):
        Label_IVP_Error.config(text=Error_x0_y0_type)
        return
    Label_IVP_Error.config(text="")
    x0v = float(x0s)
    y0v = float(y0s)
    # Check X
    Xs = str(Entry_X.get())
    if not isfloat(Xs):
        Label_X_Error.config(text=Error_X_type)
        return
    Xv = float(Xs)
    if x0v >= Xv:
        Label_X_Error.config(text=Error_X_less_than_x0)
        return
    Label_X_Error.config(text="")
    # Check N
    mode = OneNVar.get()
    if mode:
        N0s = str(Entry_N.get())
        if not N0s.isdecimal():
            Label_N_Error.config(text=Error_OneN_type)
            return
        N0v = int(N0s)
        Nkv = N0v
        if N0v <= 0:
            Label_N_Error.config(text=Error_OneN_type)
            return
    else:
        N0s = str(Entry_N0.get())
        Nks = str(Entry_Nk.get())
        if not (N0s.isdecimal() and Nks.isdecimal()):
            Label_Range_Error.config(text=Error_MultipleN_type)
            return
        N0v = int(N0s)
        Nkv = int(Nks)
        if not (N0v > 0 and Nkv > 0):
            Label_Range_Error.config(text=Error_MultipleN_type)
            return
        if N0v >= Nkv:
            Label_Range_Error.config(text=Error_MultipleN_invalid_range)
            return
    Label_N_Error.config(text="")
    Label_Range_Error.config(text="")
    if InitFunction(x0v, y0v):
        Label_IVP_Error.config(text=Error_Overflow)
        return
    Execute(x0v, y0v, Xv, N0v, Nkv,
            mode or MultipleN_PlotValuesVar.get(), mode and OneN_PlotValues_AutoOpenVar.get(),
            (mode and OneN_PlotErrorsVar.get()) or ((not mode) and MultipleN_PlotErrorsVar.get()),
            mode and OneN_PlotErrors_AutoOpenVar.get(),
            not mode, MultipleN_PlotDependence_AutoOpenVar.get())
