from presenter import CalculatorPresenter
from tkinter import *
from tkinter import ttk


class CalculatorView:
    def __init__(self):
        self.presenter = CalculatorPresenter(self)
        self.options = ("?", "H", "F(x)")
        self.first = ("(", ")", "C", "<=")
        self.second = ("ln()", "log()", "mod", "x^")
        self.third = ("sin()", "cos()", "tan()", "sqrt()")
        self.fourth = ("asin()", "acos()", "atan()", "F(x)")
        self.fifth = ("7", "8", "9", "*")
        self.sixth = ("4", "5", "6", "/")
        self.seventh = ("1", "2", "3", "-")
        self.eighth = (".", "0", "=", "+")
        self.ninth = (" ", "PN", "RPN", "Default")

        self.rows = (self.first, self.second, self.third,
                     self.fourth, self.fifth, self.sixth,
                     self.seventh, self.eighth, self.ninth)

        self.parentheses_funcs = self.second[:2:] + self.third + self.fourth[:3:]
        self.except_funcs = ("C", "<=", "=", "x^", "mod")
        self.modes = ("PN", "RPN", "Default")

        self.frames = []
        self.buttons = {}

        self.root = Tk()
        self.frames.append(self.make_frame())
        self.input_field = Entry(self.frames[0])
        self.btn_style = ttk.Style()
        self.btn_style.configure('my.TButton', font=('Helvetica', 12))

    def create_window(self):
        self.root.title("SmartCalc v3.0")
        self.root.geometry("400x290+670+130")       # windows
        # self.root.geometry("300x250+300+200")       # mac

    def make_frame(self):
        frame = Frame(self.root)
        frame.pack()
        return frame

    def create_gui(self):
        self.create_options()
        self.create_entry_field()
        self.create_rows_of_buttons()

    def create_options(self):
        for option in self.options:
            btn = ttk.Button(self.frames[0])
            btn["text"] = option
            btn["style"] = 'my.TButton'
            btn["width"] = 3
            btn.pack(side=LEFT)
            self.buttons[option] = btn

    def create_entry_field(self):
        validate_cmd = (self.root.register(self.presenter.validate_input), '%d', '%S')
        invalid_cmd = (self.root.register(self.presenter.invalid_input), '%S')

        self.input_field["validate"] = 'key'
        self.input_field["justify"] = RIGHT
        self.input_field["validatecommand"] = validate_cmd
        self.input_field["invalidcommand"] = invalid_cmd
        self.input_field["width"] = 30
        self.input_field["font"] = ("Helvetica", 20)
        self.input_field.pack(anchor=W, side=LEFT)

    def create_rows_of_buttons(self):
        for row in self.rows:
            self.frames.append(self.make_frame())
            for sym in row:
                self.create_button(self.frames[-1], sym)

    def create_button(self, frame, txt):
        btn = ttk.Button(frame)
        btn["text"] = txt
        btn["style"] = 'my.TButton'

        btn["state"] = [DISABLED
                        if txt in ["Default", " ", "F(x)"]
                        else NORMAL]

        btn["command"] = lambda: [self.change_mode(txt)
                                  if txt in self.modes
                                  else self.write_or_use(txt)]
        btn.pack(side=LEFT)
        self.buttons[txt] = btn

    def write_or_use(self, btn):
        if btn not in self.except_funcs:
            self.write_to_field(btn)
            if btn in self.parentheses_funcs:
                self.presenter.model.delete_symbol(self.input_field.get())
        else:
            self.presenter.preprocessor(btn)

    def write_to_field(self, txt):
        index = len(self.input_field.get())
        self.input_field.insert(index, txt)

    # def start_new(self):
    #     if (entry.event in ["+", "-", "*", "/"]):
    #         write_to_field()
    #     else:
    #         self.presenter.model.clear_expression()
    #         write_to_field()

    def change_mode(self, mode):
        if mode == "PN":
            self.pn_button_handler()
        if mode == "RPN":
            self.rpn_button_handler()
        if mode == "Default":
            self.default_button_handler()

    def parentheses_funcs_switch(self, mode):
        for btn in self.parentheses_funcs:
            self.buttons[btn]["state"] = mode

    def pn_button_handler(self):
        self.presenter.polish_notation = True
        self.presenter.reverse_polish_notation = False
        self.buttons[" "]["state"] = NORMAL
        self.buttons["PN"]["state"] = DISABLED
        self.buttons["RPN"]["state"] = NORMAL
        self.buttons["Default"]["state"] = NORMAL
        self.parentheses_funcs_switch(DISABLED)
        self.presenter.model.clear_expression()

    def rpn_button_handler(self):
        self.presenter.reverse_polish_notation = True
        self.presenter.polish_notation = False
        self.buttons[" "]["state"] = NORMAL
        self.buttons["PN"]["state"] = NORMAL
        self.buttons["RPN"]["state"] = DISABLED
        self.buttons["Default"]["state"] = NORMAL
        self.parentheses_funcs_switch(DISABLED)
        self.presenter.model.clear_expression()

    def default_button_handler(self):
        self.presenter.polish_notation = False
        self.presenter.reverse_polish_notation = False
        self.buttons[" "]["state"] = DISABLED
        self.buttons["PN"]["state"] = NORMAL
        self.buttons["RPN"]["state"] = NORMAL
        self.buttons["Default"]["state"] = DISABLED
        self.parentheses_funcs_switch(NORMAL)
        self.presenter.model.clear_expression()

    def run(self):
        self.create_window()
        self.create_gui()
        self.root.mainloop()
