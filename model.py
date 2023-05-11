from math import *

class CalculatorModel:
    def __init__(self, presenter):
        self.presenter = presenter

    def print_result(self, result):
        if result - int(result):
            self.presenter.set_result(result)
        else:
            self.presenter.set_result(int(result))

    def calculate_expression(self, expression):
        try:
            result = eval(expression)
            return result
        except ZeroDivisionError:
            self.presenter.set_result("Infinity")
        except SyntaxError:
            self.presenter.set_result("error")
        except ValueError:
            self.presenter.set_result("NaN")

    def polish_calculate(self, tokens):
        stack = []
        i = 0
        # for token in tokens:
        while i < len(tokens):
            if tokens[i].isdigit():
                stack.append(tokens[i])
            elif tokens[i] in ["+", "-", "*", "/", "%", "**"]:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.calculate_expression(f"{operand1} {tokens[i]} {operand2}")
                stack.append(result)
            elif tokens[i] == "(":
                # open_ind = expression.find("(")
                # close_ind = expression.find(")")
                # cropped_expression = expression[open_ind + 1:close_ind:]
                # if cropped_expression.count("("):
                #     for i in range(expression.count("(") - 1):
                #         close_ind = expression.find(")", close_ind + 1)     #( + 4 ( + ( + 4 5 ) ( + 4 5 ) ) )
                #     cropped_expression = expression[open_ind + 1:close_ind:]
                # tkns = self.presenter.parse_expression(cropped_expression)
                # stack.append(self.polish_calculate(tkns, cropped_expression))
                # expression = expression[close_ind + 1:]
                # i += len(tkns)
                open_ind = tokens.index("(")
                close_ind = tokens.index(")")
                tkns = tokens[open_ind + 1:close_ind:]
                if tkns.count("("):
                    for i in range(tokens.count("(") - 1):
                        close_ind = tokens.index(")", close_ind + 1)  # ( + 4 ( + ( + 4 5 ) ( + 4 5 ) ) )
                    tkns = tokens[open_ind + 1:close_ind:]
                stack.append(self.polish_calculate(tkns))
                i += len(tkns)
            i += 1
        if len(stack) == 1:
            return stack.pop()

    def clear_expression(self):
        self.presenter.set_result("")

    def delete_symbol(self, input_string):
        self.presenter.set_result(input_string[:-1])
