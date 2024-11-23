"""
В этом модуле происходят все вычисления.
"""

import ast
from math import *
from typing import Union

import numpy as np
import simpleeval
from simpleeval import SimpleEval, safe_power, simple_eval


class Model:

    def __init__(self):
        self.s = SimpleEval()
        self.s.operators[ast.BitXor] = safe_power

        self.s.functions.update({"sin": np.sin,
                                 "cos": np.cos,
                                 "tan": np.tan,
                                 "asin": np.arcsin,
                                 "acos": np.arccos,
                                 "atan": np.arctan,
                                 "sqrt": np.sqrt,
                                 "ln": log,
                                 "log": log10
                                 })

    def set_x(self, x) -> None:
        self.s.names["x"] = x

    def calculate_expression(self, expression: str) -> Union[int, float, str]:
        try:
            return self.get_result(expression)
        except ZeroDivisionError:
            return "Infinity"
        except SyntaxError:
            return "error"
        except TypeError:
            return "error"
        except simpleeval.InvalidExpression:
            return "invalid_expression"
        except Exception:
            return "unknown_error"

    def get_result(self, expression: str) -> Union[int, float]:
        return self.s.eval(expression)

    def polish_calculate(self, tokens: list, reverse_pn: bool) -> Union[int, float]:
        """Алгоритм вычисления выражений в Польской нотации"""

        stack = []
        i = 0

        while i < len(tokens):
            if tokens[i].isdigit() or tokens[i][1:].isdigit():
                stack.append(tokens[i])
            elif tokens[i] in ["+", "-", "*", "/", "%", "**"]:
                stack.append(self.get_polish_result(operator=tokens[i], stack=stack, reverse_pn=reverse_pn))
            elif tokens[i] == "(":
                i += self.polish_paranthesis(tokens, stack)
            i += 1
        if len(stack) == 1:
            return stack.pop()

    def get_polish_result(self, operator: str, stack: list, reverse_pn: bool) -> Union[int, float, str]:
        """Вычисляет результат одной операции в польской нотации"""
        if len(stack) > 1:
            operand1 = stack.pop()
            operand2 = stack.pop()

            if reverse_pn:
                operand1, operand2 = operand2, operand1

            expression = f"{operand1} {operator} {operand2}"
        else:
            operand = stack.pop()
            expression = f"{operator} {operand}"

        return self.calculate_expression(expression)

    def polish_paranthesis(self, tokens: list, stack: list) -> Union[int, float]:
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