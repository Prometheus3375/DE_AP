from tkinter import *


# Globals
BoxWidth = 18
XSpaceBetweenPx = 15
YSpaceBetweenPx = 10
MainWindowOffset = 10
IntEntryWidth = 4
RealEntryWidth = 8
# Misc
AllFrames = []


def Bool2State(b: bool) -> str:
    if b:
        return NORMAL
    return DISABLED


class GUIObject:
    def __init__(self, x: int, y: int, endx: int, endy: int, enable: bool):
        self.x = x
        self.y = y
        self.endx = endx
        self.endy = endy
        self.enabled = enable

    def Switch(self, enable: bool) -> None:
        self.enabled = enable

    def GetWidth(self) -> int:
        return self.endx - self.x + 1

    def GetHeight(self) -> int:
        return self.endy - self.y + 1


class Point(GUIObject):
    SpacePx = 5

    def __init__(self, x: int, y: int, lab_text: str, charn: int, ent_text: str, enable: bool=True):
        state = Bool2State(enable)
        # Make label
        self.label = Label(text=lab_text, state=state)
        self.label.place(x=x, y=y)
        l_width = x + self.label.winfo_reqwidth() - 1 + Point.SpacePx
        # Make entry
        self.entry = Entry(width=charn)
        self.entry.place(x=l_width, y=y)
        self.entry.insert(0, ent_text)
        self.entry.config(state=state)
        # Common
        GUIObject.__init__(self, x, y,
                           l_width + self.entry.winfo_reqwidth() - 1,
                           y + max(self.label.winfo_reqheight(), self.entry.winfo_reqheight()) - 1,
                           enable)

    def Switch(self, enable: bool) -> None:
        state = Bool2State(enable)
        self.label.config(state=state)
        self.entry.config(state=state)
        GUIObject.Switch(self, enable)


class LabelExt(GUIObject):
    TextColor = "#000000"
    Text = ""

    def __init__(self, x: int, y: int, text: str=Text, fg: str=TextColor, enable: bool=True):
        # Make label
        self.label = Label(text=text, fg=fg, state=Bool2State(enable))
        self.label.place(x=x, y=y)
        # Common
        GUIObject.__init__(self, x, y,
                           x + self.label.winfo_reqwidth() - 1,
                           y + self.label.winfo_reqheight() - 1,
                           enable)

    def Switch(self, enable: bool) -> None:
        self.label.config(state=Bool2State(enable))
        GUIObject.Switch(self, enable)


class StaticRadioButton(GUIObject):
    def __init__(self, x: int, y: int, text: str, enable: bool=True):
        self.button = Radiobutton(text=text, state=Bool2State(enable), takefocus=False)
        self.button.place(x=x, y=y)
        # Common
        GUIObject.__init__(self, x, y,
                           x + self.button.winfo_reqwidth() - 1,
                           y + self.button.winfo_reqheight() - 1,
                           enable)

    def Switch(self, enable: bool) -> None:
        self.button.config(state=Bool2State(enable))
        GUIObject.Switch(self, enable)


class CheckButtonExt(GUIObject):
    def __init__(self, text: str, variable: BooleanVar, x: int, y: int, parent=None, command=None, enable: bool=True):
        if not(parent is None):
            x = parent.x + BoxWidth
            y = parent.endy
            enable = parent.enabled and parent.GetVal() and enable
        self.button = Checkbutton(text=text, variable=variable, onvalue=True, offvalue=False,
                                  command=command, state=Bool2State(enable))
        self.button.place(x=x, y=y)
        # Common
        GUIObject.__init__(self, x, y,
                           x + self.button.winfo_reqwidth() - 1,
                           y + self.button.winfo_reqheight() - 1,
                           enable)
        self.parent = parent
        self.var = variable

    def Switch(self, enable: bool) -> None:
        if not(self.parent is None):
            enable = self.parent.enabled and self.parent.GetVal() and enable
        self.button.config(state=Bool2State(enable))
        GUIObject.Switch(self, enable)

    def GetVal(self) -> bool:
        return self.var.get()


class FrameExt(GUIObject):
    FrameBorderWidthPx = 2
    XLabelOffsetPx = 4
    XTextOffsetPx = 3
    YTextOffsetPx = 21

    def __init__(self, x: int, y: int, width: int=0, height: int=0,
                 labelwidget: Widget=None, text: str=None, bd: int=FrameBorderWidthPx, enable: bool=True):
        self.frame = LabelFrame(width=width, height=height, labelwidget=labelwidget, text=text, bd=bd)
        self.frame.place(x=x, y=y)
        # Init coordinates
        uselable = text is None
        if uselable:
            self.offx = bd - 1 + FrameExt.XLabelOffsetPx
        else:
            self.offx = bd - 1 + FrameExt.XTextOffsetPx
        self.xint = x + self.offx
        if uselable:
            self.offy = max(labelwidget.winfo_reqheight(), bd) - 1
        else:
            self.offy = max(FrameExt.YTextOffsetPx, bd) - 1
        self.yint = y + self.offy
        # Common
        GUIObject.__init__(self, x, y,
                           x + width - 1,
                           y + height - 1,
                           enable)
        # Add to frames list
        AllFrames.append(self)
        # Init internal widgets
        self.widgets = []

    def ResizeX(self, endx: int) -> None:
        self.endx = self.offx * 2 + endx
        self.frame.config(width=self.GetWidth())

    def ResizeY(self, endy: int) -> None:
        self.endy = self.offy // 2 + endy
        self.frame.config(height=self.GetHeight())

    def ResizeXSimple(self) -> None:
        self.endx = self.offx * 2 + max([w.endx for w in self.widgets])
        self.frame.config(width=self.GetWidth())

    def ResizeYSimple(self) -> None:
        self.endy = self.offy // 2 + max([w.endy for w in self.widgets])
        self.frame.config(height=self.GetHeight())

    def Switch(self, enable: bool) -> None:
        for w in self.widgets:
            w.Switch(enable)
        GUIObject.Switch(self, enable)

    def AddPoint(self, lab_text: str, charn: int, ent_text: str,
                 x: int=0, y: int=0, enable: bool=True) -> Point:
        p = Point(max(self.xint, x), max(self.yint, y), lab_text, charn, ent_text, enable=(enable and self.enabled))
        self.widgets.append(p)
        return p

    def AddLabel(self, text: str=LabelExt.Text, fg: str=LabelExt.TextColor,
                 x: int=0, y: int=0, enable: bool=True) -> LabelExt:
        l = LabelExt(max(self.xint, x), max(self.yint, y), text=text, fg=fg, enable=(enable and self.enabled))
        self.widgets.append(l)
        return l

    def AddStaticRadioButton(self, text: str,
                             x: int=0, y: int=0, enable: bool=True) -> StaticRadioButton:
        b = StaticRadioButton(max(self.xint, x), max(self.yint, y), text, enable=(enable and self.enabled))
        self.widgets.append(b)
        return b

    def AddCheckButton(self, text: str, variable: BooleanVar, parent: CheckButtonExt=None,
                    x: int=0, y: int=0, command=None, enable: bool=True) -> CheckButtonExt:
        b = CheckButtonExt(text, variable,
                           max(self.xint, x), max(self.yint, y), parent=parent,
                           command=command, enable=(enable and self.enabled))
        self.widgets.append(b)
        return b


def SimpleButton(x: int, y: int, text: str, width: int, height: int, command) -> None:
    button = Button(text=text, width=width, height=height, command=command)
    y -= button.winfo_reqheight() // 2
    button.place(x=x, y=y)
