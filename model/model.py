""" Этот модуль представляет часть проекта под названием Модель.
Согласно принципам ModelViewPresenter здесь происходят все вычисления.
"""

from typing import Any
from math import *
import numpy as np


class CalculatorModel:
    def __init__(self, presenter=None):
        self.presenter = presenter
        self.result = None

    def set_error_to_entry(self, error):
        self.presenter.set_error_to_entry(error)

    def calculate_expression(self, expression: str, x: Any = 0) -> int:
        """Eval используется для вычисления всех выражений.
        Безопасность обеспечивается запретом на ввод символов в
        entry-поле с клавиатуры"""
        try:
            self.result = eval(expression)
            return self.result
        except ZeroDivisionError:
            self.set_error_to_entry("Infinity")
            raise
        except SyntaxError:
            self.set_error_to_entry("error")
            raise
        except ValueError:
            self.set_error_to_entry("NaN")
            raise
        except TypeError:
            self.set_error_to_entry("error")
            raise
        except Exception:
            self.set_error_to_entry("Unknown error")
            raise

    def polish_calculate(self, tokens: list) -> int:
        """Алгоритм вычисления выражений в Польской нотации"""

        def get_polish_result(stack):
            """Вычисляет результат одной операции в польской нотации"""
            if len(stack) > 1:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.calculate_expression(
                    f"{operand1} {tokens[i]} {operand2}")
            else:
                operand = stack.pop()
                result = self.calculate_expression(
                    f"{tokens[i]} {operand}")
            return result

        def polish_paranthesis(tokens, stack):
            """Обрабатывает и вычисляет выражения внутри скобок"""
            open_ind = tokens.index("(")
            close_ind = tokens.index(")")
            tkns = tokens[open_ind + 1:close_ind:]
            if tkns.count("("):
                for _ in range(tokens.count("(") - 1):
                    close_ind = tokens.index(")", close_ind + 1)
                tkns = tokens[open_ind + 1:close_ind:]
            stack.append(self.polish_calculate(tkns))
            return len(tkns)

        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i].isdigit() or tokens[i][1:].isdigit():
                stack.append(tokens[i])
            elif tokens[i] in ["+", "-", "*", "/", "%", "**"]:
                stack.append(get_polish_result(stack))
            elif tokens[i] == "(":
                i += polish_paranthesis(tokens, stack)
            i += 1
        if len(stack) == 1:
            return stack.pop()

    def plot(self, fixed_expr: str) -> None:
        """Вычисляет х и у для построения графика"""
        self.presenter.x = np.linspace(-10000, 10000)
        self.presenter.y = self.calculate_expression(fixed_expr,
                                                     self.presenter.x)
