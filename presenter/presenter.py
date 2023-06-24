"""" Presenter является посредником между
интерфейсом и моделью. Здесь происходит большая часть
обработок и преобразований.
"""

from presenter.utils import *
from typing import Any
import matplotlib.pyplot as plt
from model.model import CalculatorModel


class CalculatorPresenter:

    def __init__(self, view):
        self.view = view
        self.model = CalculatorModel(self)

        self.polish_notation = False
        self.reverse_polish_notation = False

        self.plot_x = 0
        self.plot_y = 0

    def get_input_field(self) -> str:
        return self.view.input_field.get()

    def set_error_to_entry(self, error: str) -> None:
        """ Устанавливает ошибку в entry-поле калькулятора """
        self.view.set_to_field(error)

    def clear_expression(self) -> None:
        """Очищает entry-поле"""
        self.view.set_to_field("")

    def delete_symbol(self, input_field: str) -> None:
        """Удаляет символ(ы) в entry-поле"""
        qua = check_before_del(input_field, self.view.parentheses_funcs)
        self.view.set_to_field(input_field[:qua])

    def result_handling(self, result: Any) -> None:
        if result not in self.view.err_messages:
            result = floats_handling(result)
        self.view.set_to_field(result)

    def validate_input(self, type_of_change: str, changed_str: str) -> bool:
        """Проверка на некорректное изменение"""
        if type_of_change == '-1':
            self.result_handling("error")
            return False
        if changed_str.find(" ") != -1:
            if not self.polish_notation \
                    and not self.reverse_polish_notation:
                return False
        return True

    def invalid_input(self) -> None:
        """Запускается в случае невалидного содержимого entry-поля"""
        self.clear_expression()

    def preprocessor(self, btn: str) -> None:
        input_field = self.get_input_field()
        if input_field == "":
            return

        if btn == "=":
            if not paranthesis_check(input_field):
                return
            self.view.view_proc.history.add_expression(input_field)

        self.processor(btn, input_field)

    def processor(self, btn: str, input_field: str) -> None:
        """Определяет дальнейшие действия в зависимости нажатой кнопки"""
        if btn == "=":
            self.which_notation(input_field)
        if btn == "C":
            self.clear_expression()
        if btn == "CE":
            self.delete_symbol(input_field)
        if btn == "x^":
            self.view.add_to_field("**")
        if btn == "mod":
            self.view.add_to_field("%")

    def which_notation(self, input_field):
        if self.polish_notation or self.reverse_polish_notation:
            self.polish_precalculate(input_field)
        else:
            self.infix_precalculate(input_field)

    def polish_precalculate(self, input_field: str):
        """Производит корректировку выражения перед вычислением"""

        if self.polish_notation is True:
            input_field = reverse_expression(input_field)
        tokens = input_field.split()
        if not tokens[0].isdigit() and not tokens[0][1:].isdigit():
            self.set_error_to_entry("error")
        else:
            result = self.model.polish_calculate(tokens)
            self.result_handling(result)

    def infix_precalculate(self, input_field: str) -> None:
        """Производит корректировку выражения перед вычислением"""
        def correct_string(input_field: str) -> str:
            """Запускает корректировку строки"""
            corrected_str = paranthesis_handling(input_field)
            return log_handling(corrected_str)

        corrected_string = correct_string(input_field)
        result = self.model.calculate_expression(corrected_string)
        self.result_handling(result)
