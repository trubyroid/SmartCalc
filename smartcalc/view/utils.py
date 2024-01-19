from tkinter import Frame
from typing import Union

from view.help import Help
from view.history import History
from view.main_window import MainWindow

MAIN_WINDOWS_FRAMES = 11
HISTORY_FRAMES = 2
DEFAULT_FRAMES = 0

def create_window(obj: Union[MainWindow,
                             Help,
                             History]) -> None:
    obj.tk_window.title(obj.name)
    obj.tk_window.geometry(obj.geometry)
    obj.tk_window.mainloop()


def make_frames(section: Union[MainWindow,
                               Help,
                               History]) -> None:
    if section.name == "SmartCalc v3.0":
        quantity = MAIN_WINDOWS_FRAMES
    elif section.name == "History":
        quantity = HISTORY_FRAMES
    else:
        quantity = DEFAULT_FRAMES

    for _ in range(quantity):
        new_frame = Frame(section.tk_window)
        new_frame.pack()
        section.frames.append(new_frame)