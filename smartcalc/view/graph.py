"""
В этом модуле производится подготовка и построение графика функции
"""

import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt
import numpy as np
from presenter.utils import paranthesis_check

LOWER_LIMIT = -1000000
UPPER_LIMIT = 1000000

class Graph:
    def __init__(self, view) -> None:
        self.view = view
        self.tk_window = self.view.tk_window

        self.range_dialog = None
        self.plot = None
        self.x_entry = None
        self.y_entry = None

        self.x_range = ()
        self.y_range = ()

    def graph_preparing(self) -> None:
        expression = self.view.input_field.get()
        if not paranthesis_check(expression):
            return

        self.range_dialog = tk.Toplevel(self.tk_window)
        self.range_dialog.title("Ranges for graph")

        x_label = tk.Label(self.range_dialog, 
                           text="Definition range (begin, end): ")
        x_label.grid(row=0, column=0, padx=10, pady=5)
        self.x_entry = tk.Entry(self.range_dialog)
        self.x_entry.grid(row=0, column=1, padx=10, pady=5)

        y_label = tk.Label(self.range_dialog, 
                           text="Range of function values (begin, end): ")
        y_label.grid(row=1, column=0, padx=10, pady=5)
        self.y_entry = tk.Entry(self.range_dialog)
        self.y_entry.grid(row=1, column=1, padx=10, pady=5)

        confirm_btn = tk.Button(self.range_dialog, text="Approve",
                                command=lambda: self.get_ranges(expression))

        confirm_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def get_ranges(self, expression: str) -> None:
        x_range_str = self.x_entry.get()
        y_range_str = self.y_entry.get()
        try:
            x_start, x_end = map(float, x_range_str.split(','))
            y_start, y_end = map(float, y_range_str.split(','))

            if x_start < LOWER_LIMIT \
                    or y_start < LOWER_LIMIT \
                    or x_end > UPPER_LIMIT \
                    or y_end > UPPER_LIMIT:
                raise ValueError

            self.x_range = (x_start, x_end)
            self.y_range = (y_start, y_end)
            self.range_dialog.destroy()

            self.create_graph(expression)

        except ValueError:
            messagebox.showerror("Error", "Invalid range(s)")

    def create_graph(self, expression: str) -> None:
        if self.x_range and self.y_range:

            x = np.linspace(self.x_range[0], self.x_range[1], 1000)

            self.view.presenter.set_x_to_model(x)

            y = self.view.presenter.send_to_model(
                expression)

            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('sin(x)')
            plt.xlim(self.x_range[0], self.x_range[1])
            plt.ylim(self.y_range[0], self.y_range[1])
            plt.title('Function graph ' + expression)
            plt.grid(True)

            plt.show()
