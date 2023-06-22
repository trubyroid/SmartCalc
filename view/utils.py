from view.main_window import CalculatorMain
from view.history import CalculatorHistory
from view.help import CalculatorHelp
from tkinter import Frame
from typing import Union


def create_window(obj: Union[CalculatorMain,
                             CalculatorHelp,
                             CalculatorHistory]) -> None:
    obj.tk_window.title(obj.name)
    obj.tk_window.geometry(obj.geometry)
    obj.tk_window.mainloop()


def make_frames(section: Union[CalculatorMain,
                               CalculatorHelp,
                               CalculatorHistory]) -> None:
    if section.name == "SmartCalc v3.0":
        quantity = 11
    elif section.name == "History":
        quantity = 2
    else:
        quantity = 0

    for _ in range(quantity):
        new_frame = Frame(section.tk_window)
        new_frame.pack()
        section.frames.append(new_frame)