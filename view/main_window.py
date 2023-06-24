"""В этом модуле находится всё что связано
с интерфейсом главного окна калькулятора."""

from tkinter import ttk
from tkinter import Entry, Frame
from tkinter import W, DISABLED, NORMAL, RIGHT, LEFT, END
from typing import Callable
from presenter.presenter import CalculatorPresenter


class CalculatorMain:
    def __init__(self, view_proc):
        self.view_proc = view_proc
        self.presenter = CalculatorPresenter(self)

        self.tk_window = None
        self.input_field = None
        self.btn_style = None
        self.buttons = {}
        self.frames = []

        self._name = "SmartCalc v3.0"
        # self._geometry = "300x280+700+200"
        self._geometry = "400x320+700+200"

        self._options = ("?", "H", "F(x)")
        self._first = ("(", ")", "C", "CE")
        self._second = ("sin()", "cos()", "tan()", "x")
        self._third = ("asin()", "acos()", "atan()", "sqrt()")
        self._fourth = ("ln()", "log()", "mod", "x^")
        self._fifth = ("7", "8", "9", "*")
        self._sixth = ("4", "5", "6", "/")
        self._seventh = ("1", "2", "3", "-")
        self._eighth = (".", "0", "=", "+")
        self._ninth = (" ", "PN", "RPN", "Default")

        self.rows = (
            self._first, self._second, self._third,
            self._fourth, self._fifth, self._sixth,
            self._seventh, self._eighth, self._ninth
        )

        self._err_messages = ("Infinity", "NaN", "error", "Unknown error")

        self.parentheses_funcs = self._second[:3:]\
            + self._third + self._fourth[:2:]

        self.except_funcs = ("C", "CE", "=", "x^", "mod")
        self.modes = ("PN", "RPN", "Default")

    @property
    def name(self) -> str:
        return self._name

    @property
    def geometry(self) -> str:
        return self._geometry\

    @property
    def err_messages(self) -> tuple:
        return self._err_messages

    def create_gui(self) -> None:
        def configure_style() -> None:
            self.btn_style = ttk.Style()
            self.btn_style.configure('my.TButton', font=('Helvetica', 12))

        configure_style()
        self.create_options()
        self.create_entry_field()
        self.create_rows_of_buttons()

    def create_options(self) -> None:
        for option in self._options:
            self.create_button(self.frames[0], option)

    def create_entry_field(self) -> None:
        self.input_field = Entry(self.frames[1])

        validate_cmd = (self.tk_window.register
                        (self.presenter.validate_input), '%d', '%S')
        invalid_cmd = (self.tk_window.register
                       (self.presenter.invalid_input), '%S')

        self.input_field["validate"] = 'key'
        self.input_field["justify"] = RIGHT
        self.input_field["validatecommand"] = validate_cmd
        self.input_field["invalidcommand"] = invalid_cmd
        self.input_field["width"] = 30
        self.input_field["font"] = ("Helvetica", 20)
        self.input_field.bind("<Key>", lambda e: "break")
        self.input_field.pack(anchor=W, side=LEFT)

    def create_rows_of_buttons(self) -> None:
        i = 2
        for row in self.rows:
            for btn in row:
                self.create_button(self.frames[i], btn)
            i += 1

    def create_button(self, frame: Frame, txt: str):
        def choose_func() -> Callable[[str], None]:
            if txt in self._options:
                func = self.view_proc.use_option
            elif txt in self.modes:
                func = self.change_mode
            else:
                func = self.write_or_use
            return func

        def choose_state() -> str:
            return DISABLED if txt in ["Default", " "] else NORMAL

        btn = ttk.Button(frame)
        btn["text"] = txt
        btn["style"] = 'my.TButton'
        btn["state"] = choose_state()
        btn["command"] = lambda: choose_func()(txt)
        btn.pack(side=LEFT)
        self.buttons[txt] = btn

    def write_or_use(self, btn: str) -> None:
        if self.input_field.get() in self._err_messages:
            self.presenter.model.clear_expression()
        if btn not in self.except_funcs:
            if btn in self.parentheses_funcs:
                btn = btn[:-1]
            if len(self.input_field.get()) < 256:
                self.add_to_field(btn)
        else:
            self.presenter.preprocessor(btn)

    def set_to_field(self, line):
        self.input_field.delete(0, END)
        self.input_field.insert(0, line)

    def add_to_field(self, txt: str) -> None:
        self.input_field.insert(END, txt)

    def change_mode(self, mode: str) -> None:
        state = DISABLED
        if mode == "Default":
            self.default_button()
            state = NORMAL
        if mode == "PN":
            self.pn_button()
        if mode == "RPN":
            self.rpn_button()
        self.funcs_state_switch(state)
        self.presenter.clear_expression()

    def funcs_state_switch(self, state: str):
        for btn in self.parentheses_funcs:
            self.buttons[btn]["state"] = state
        self.buttons["F(x)"]["state"] = state

    def pn_button(self) -> None:
        self.presenter.polish_notation = True
        self.presenter.reverse_polish_notation = False
        self.buttons[" "]["state"] = NORMAL
        self.buttons["PN"]["state"] = DISABLED
        self.buttons["RPN"]["state"] = NORMAL
        self.buttons["Default"]["state"] = NORMAL

    def rpn_button(self) -> None:
        self.presenter.reverse_polish_notation = True
        self.presenter.polish_notation = False
        self.buttons[" "]["state"] = NORMAL
        self.buttons["PN"]["state"] = NORMAL
        self.buttons["RPN"]["state"] = DISABLED
        self.buttons["Default"]["state"] = NORMAL

    def default_button(self) -> None:
        self.presenter.polish_notation = False
        self.presenter.reverse_polish_notation = False
        self.buttons[" "]["state"] = DISABLED
        self.buttons["PN"]["state"] = NORMAL
        self.buttons["RPN"]["state"] = NORMAL
        self.buttons["Default"]["state"] = DISABLED
