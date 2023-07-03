"""В этом модуле запускается программа и создаются окна"""

from view.main_window import CalculatorMain
from view.history import CalculatorHistory
from view.help import CalculatorHelp
from view.graph import CalculatorGraph
from view.utils import create_window, make_frames
from tkinter import Tk
from typing import Union


class CalculatorView:
    def __init__(self):

        self.main_window = CalculatorMain(self)
        self.history = CalculatorHistory(self)
        self.help = CalculatorHelp()
        self.graph = CalculatorGraph(self.main_window)

        self.help_state = False
        self.history_state = False

    def run(self) -> None:
        self.open_section(self.main_window)

    def use_option(self, btn: str) -> None:
        if btn == "?":
            self.open_section(self.help)
        if btn == "H":
            self.open_section(self.history)
        if btn == "F(x)":
            self.graph.graph_preparing()

    def open_section(self,
                     section: Union[CalculatorMain,
                                    CalculatorHelp,
                                    CalculatorHistory]) -> None:

        def turn_flag() -> None:
            if section.name == "Help":
                self.help_state = not self.help_state
            if section.name == "History":
                self.history_state = not self.history_state

        def get_flag() -> bool:
            if section.name == "SmartCalc v3.0":
                return False
            if section.name == "Help":
                return self.help_state
            if section.name == "History":
                return self.history_state

        def on_closing() -> None:
            turn_flag()
            if section.name == "SmartCalc v3.0":
                self.history.export_history()
            if section.name == "History":
                section.frames.clear()
                section.listbox = None
            section.tk_window.destroy()

        if not get_flag():
            turn_flag()
            section.tk_window = Tk()
            make_frames(section)
            section.create_gui()
            section.tk_window.protocol("WM_DELETE_WINDOW", on_closing)
            create_window(section)
