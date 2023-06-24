import tkinter as tk
from tkinter import messagebox
from presenter.utils import paranthesis_check, plot_expression_handling
import matplotlib.pyplot as plt
import numpy as np


class CalculatorGraph:
    def __init__(self, view) -> None:
        self.view = view
        self.range_dialog = None
        self.plot = None
        self.tk_window = None
        self.x_entry = None
        self.y_entry = None

        self.x_range = 0
        self.y_range = 0

    def graph_preparing(self) -> None:
        expression = self.view.input_field.get()
        if not paranthesis_check(expression):
            return
        
        self.tk_window = self.view.tk_window

        self.range_dialog = tk.Toplevel(self.tk_window)
        self.range_dialog.title("Диапазоны для графика")

        x_label = tk.Label(self.range_dialog, 
                           text="Диапазон определения (начало, конец): ")
        x_label.grid(row=0, column=0, padx=10, pady=5)
        self.x_entry = tk.Entry(self.range_dialog)
        self.x_entry.grid(row=0, column=1, padx=10, pady=5)

        y_label = tk.Label(self.range_dialog, 
                           text="Диапазон значений функции (начало, конец): ")
        y_label.grid(row=1, column=0, padx=10, pady=5)
        self.y_entry = tk.Entry(self.range_dialog)
        self.y_entry.grid(row=1, column=1, padx=10, pady=5)

        confirm_btn = tk.Button(self.range_dialog, text="Подтвердить",
                                command=lambda: self.get_ranges(expression))

        confirm_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def get_ranges(self, expression: str) -> None:
        x_range = self.x_entry.get()
        y_range = self.y_entry.get()
        try:
            x_start, x_end = map(float, x_range.split(','))
            y_start, y_end = map(float, y_range.split(','))

            if x_start < -1000000 \
                    or y_start < -1000000 \
                    or x_end > 1000000 \
                    or y_end > 1000000:
                raise ValueError

            self.x_range = (x_start, x_end)
            self.y_range = (y_start, y_end)
            self.range_dialog.destroy()

            self.create_graph(expression)

        except ValueError:
            messagebox.showerror("Ошибка", "Неверный формат диапазона. \n\
                                 Введите числа, разделенные запятой. \n \
                                 Не менее -1000000 и не более 1000000")

    def create_graph(self, expression: str) -> None:
        if self.x_range and self.y_range:
            fixed_expression = plot_expression_handling(expression)

            x = np.linspace(self.x_range[0], self.x_range[1], 1000)
            y = self.view.presenter.model.calculate_expression(
                fixed_expression, x)

            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('sin(x)')
            plt.xlim(self.x_range[0], self.x_range[1])
            plt.ylim(self.y_range[0], self.y_range[1])
            plt.title('График функции ' + expression)
            plt.grid(True)

            plt.show()
