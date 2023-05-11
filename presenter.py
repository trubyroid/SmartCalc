from model import CalculatorModel
import tkinter


class CalculatorPresenter:
    def __init__(self, view):
        self.view = view
        self.model = CalculatorModel(self)
        self.polish_notation = False
        self.reverse_polish_notation = False

    def get_input_field(self) -> str:
        return self.view.input_field.get()

    def set_result(self, result):
        self.view.input_field.delete(0, tkinter.END)
        self.view.input_field.insert(0, result)

    def parse_expression(self, expression):
        return expression.split()

    def validate_input(self, type_of_change, changed_str) -> bool:
        def check_func(ind, line):
            cropped_line = line[ind::]
            open_ind = cropped_line.find("(")
            if open_ind == -1:
                return -1
            func = cropped_line[0:open_ind:]
            if func + "()" not in self.view.parentheses_funcs:
                return -1
            else:
                return ind + open_ind + 1
        # if len(self.get_input_field()) > 255:
        #     return False
        if changed_str in ["Infinity", "error", "NaN"]:
            return True
        if type_of_change == '-1':
            self.set_result("error")
        if type_of_change == '1':
            # for symb in list(changed_str):
            ind = 0
            while ind < len(changed_str):
                # if symb.isdigit()\
                #         or symb in ["+", "-", "*", "/", "(", ")", ".", " "]:
                #       необходимо правильно отработать нажатие нескольких знаков "."
                if changed_str[ind].isdigit() \
                        or changed_str[ind] in ("+", "-", "*", "/", "(", ")", ".", " "):
                    if changed_str[ind] == " ":
                        if not self.polish_notation and not self.reverse_polish_notation:
                            return False
                    ind += 1
                    continue
                elif changed_str[ind] in ('l', 's', 'c', 't', 'a'):
                    ind = check_func(ind, changed_str)
                    if ind != -1:
                        continue
                return False
        return True

    def invalid_input(self, invalid_string):
        for symbol in invalid_string:
            self.model.delete_symbol(symbol)

    def preprocessor(self, btn):
        input_field = self.get_input_field()
        if input_field == "":
            self.set_result("")
        else:
            self.processor(btn, input_field)

    def processor(self, btn, input_field):
        if btn == "=":
            self.precalculate(input_field)
        if btn == "C":
            self.model.clear_expression()
        if btn == "<=":
            self.model.delete_symbol(input_field)
        if btn == "x^":
            self.view.write_to_field("**")
        if btn == "mod":
            self.view.write_to_field("%")

    def paranthesis_handling(self, field_string):
        open_br_num = field_string.count("(")
        close_br_num = field_string.count(")")
        ind = -1

        def check_symb(symb):
            return True if symb.isdigit() or symb == ")" else False

        if open_br_num:
            for i in range(open_br_num + 1):
                ind = field_string.find("(", ind + 1)
                if ind - 1 >= 0 and check_symb(field_string[ind - 1]):
                    old = field_string[ind-1:ind + 1:]
                    new = field_string[ind-1] + "*" + field_string[ind]
                    field_string = field_string.replace(old, new)
                ind += 1

            for i in range(close_br_num):
                ind = field_string.find(")", ind + 1)
                if ind + 1 < len(field_string) and field_string[ind+1].isdigit():
                    old = field_string[ind:ind + 2:]
                    new = field_string[ind] + "*" + field_string[ind+1]
                    field_string = field_string.replace(old, new)
        return field_string

    def log_handling(self, field_string):
        corrected_string = field_string.replace("log", "log10")
        corrected_string = corrected_string.replace("ln", "log")
        return corrected_string

    def correct_string(self, input_field):
        corrected_string = self.paranthesis_handling(input_field)
        corrected_string = self.log_handling(corrected_string)
        return corrected_string

    def precalculate(self, input_field):
        if input_field.count("(") != input_field.count(")"):
            return
        if self.polish_notation is True:
            expression = list(input_field[::-1])
            for i in range(len(expression)):
                if expression[i] == "(":
                    expression[i] = ")"
                elif expression[i] == ")":
                    expression[i] = "("
            expression = ''.join(expression)
            tokens = self.parse_expression(expression)
            result = self.model.polish_calculate(tokens)
        elif self.reverse_polish_notation is True:
            tokens = self.parse_expression(input_field)
            result = self.model.polish_calculate(tokens)
        else:
            corrected_string = self.correct_string(input_field)
            result = self.model.calculate_expression(corrected_string)
        self.model.print_result(result)
