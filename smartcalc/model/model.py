"""
В этом модуле, согласно принципам ModelViewPresenter, происходят все вычисления.
"""

from typing import Any
from math import *
import numpy as np


class CalculatorModel:
    def __init__(self):
        ...

    def get_result(self, expression: str, x: Any = 0):
        """Eval используется для вычисления всех выражений.
        Безопасность обеспечивается запретом на ввод символов в
        entry-поле с клавиатуры"""
        return eval(expression)

    def calculate_expression(self, expression: str, x: Any = 0) -> Any:
        try:
            return self.get_result(expression, x)
        except ZeroDivisionError:
            return "Infinity"
        except SyntaxError:
            return "error"
        except ValueError:
            return "NaN"
        except TypeError:
            return "error"
        except Exception:
            return "Unknown error"

    def polish_calculate(self, tokens: list) -> int:
        """Алгоритм вычисления выражений в Польской нотации"""

        def get_polish_result(stack):
            """Вычисляет результат одной операции в польской нотации"""
            if len(stack) > 1:
                operand2 = stack.pop()
                operand1 = stack.pop()
                expression = f"{operand1} {tokens[i]} {operand2}"
            else:
                operand = stack.pop()
                expression = f"{tokens[i]} {operand}"

            return self.calculate_expression(expression)

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
