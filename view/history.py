import pickle
from tkinter import NW, X, END, LEFT
from tkinter import ttk
from tkinter import Listbox
from tkinter import messagebox
from tkinter.messagebox import askyesno


class CalculatorHistory:
    def __init__(self, view):
        self.view = view.main_window
        self.tk_window = None
        self.listbox = None
        self.btn_style = None

        self._geometry = "400x280+1000+200"
        self._name = "History"
        self._buttons = ("Add to calc", "Delete", "Clear history")
        self._history_filename = 'history.pickle'

        self._operations = []
        self.frames = []
        self.import_history()

    @property
    def name(self) -> str:
        return self._name

    @property
    def geometry(self) -> str:
        return self._geometry

    @property
    def operations(self) -> list:
        return self._operations

    def create_gui(self) -> None:
        def configure_style():
            self.btn_style = ttk.Style()
            self.btn_style.configure('my.TButton', font=('Helvetica', 12))

        configure_style()

        self.create_listbox()
        self.insert_expressions()
        self.create_buttons()

    def create_listbox(self) -> None:
        self.listbox = Listbox(self.frames[0])
        self.listbox["height"] = 11
        self.listbox["width"] = 125
        self.listbox["fg"] = "black"
        self.listbox["selectbackground"] = "blue"
        self.listbox["font"] = ('Helvetica', 17)
        self.listbox.pack(anchor=NW, fill=X, padx=5, pady=5)

    def insert_expressions(self) -> None:
        for expression in self.operations:
            self.listbox.insert(END, expression)

    def create_buttons(self) -> None:
        for name in self._buttons:
            self.create_button_widget(name)

    def create_button_widget(self, name: str) -> None:
        def choose_func(btn_name: str) -> None:
            if btn_name == "Clear history":
                result = askyesno("History clearing", "Are you sure?")
                if result:
                    self.clear_history()
            else:
                self.add_or_delete(btn_name)

        btn = ttk.Button(self.frames[1])
        btn["text"] = name
        btn["style"] = 'my.TButton'
        btn["command"] = lambda: choose_func(name)
        btn.pack(side=LEFT)

    def clear_history(self) -> None:
        self._operations = []
        self.listbox.delete(0, last=END)

    def add_or_delete(self, btn: str) -> None:
        selection = self.listbox.curselection()
        if selection == ():
            messagebox.showerror("Error", "Operation not selected.")
            return

        if btn == "Add to calc":
            self.add_to_calculator(selection[0])
        if btn == "Delete":
            self.delete_expression(selection[0])

    def add_to_calculator(self, index: int) -> None:
        self.view.set_to_field(self.operations[index])

    def delete_expression(self, expression: str) -> None:
        self.listbox.delete(expression)

    def add_expression(self, expression: str) -> None:
        self._operations.append(expression)
        if self.listbox:
            self.listbox.insert(END, expression)

    def import_history(self) -> None:
        with open(self._history_filename, 'rb') as file:
            self._operations = pickle.load(file)

    def export_history(self) -> None:
        with open(self._history_filename, 'wb') as file:
            pickle.dump(self._operations, file)
