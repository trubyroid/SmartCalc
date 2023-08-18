from typing import Any


def paranthesis_handling(field_string: str) -> str:
    """Добавляет знаки умножения перед/после скобок, если их не было"""
    open_braces = field_string.count("(")
    close_braces = field_string.count(")")
    ind = -1

    def check_symbol(symbol: str) -> bool:
        return True if symbol.isdigit() or symbol == ")" else False

    if open_braces:
        for _ in range(open_braces + 1):
            ind = field_string.find("(", ind + 1)
            if ind - 1 >= 0 and check_symbol(field_string[ind - 1]):
                old = field_string[ind - 1:ind + 1:]
                new = field_string[ind - 1] + "*" + field_string[ind]
                field_string = field_string.replace(old, new)
            ind += 1

        for _ in range(close_braces):
            ind = field_string.find(")", ind + 1)
            if ind + 1 < len(field_string) \
                    and field_string[ind + 1].isdigit():
                old = field_string[ind:ind + 2:]
                new = field_string[ind] + "*" + field_string[ind + 1]
                field_string = field_string.replace(old, new)
    return field_string


def handling_for_eval(expr: str) -> str:
    """Видоизменяет строку перед тем, как она попадет в eval"""
    return expr.\
        replace("log", "log10").\
        replace("ln", "log").\
        replace("^", "**").\
        replace("mod", "%")


def correct_expression(expression: str) -> str:
    corrected_str = paranthesis_handling(expression)
    corrected_str = handling_for_eval(corrected_str)
    return corrected_str


def plot_expression_handling(expression: str) -> str:
    """Корректирует выражение"""
    fixes_one = {
        "asin": "np.arcsin",
        "acos": "np.arccos",
        "atan": "np.arctan",
        "sin": "np.sin",
        "cos": "np.cos",
        "tan": "np.tan",
        "sqrt": "np.sqrt",
        "log": "np.log",
        "ln": "np.ln"
    }
    fixes_two = {
        "arcnp.sin": "arcsin",
        "arcnp.cos": "arccos",
        "arcnp.tan": "arctan",
    }
    fixed_expr = expression
    for key, val in fixes_one.items():
        fixed_expr = fixed_expr.replace(key, val)
    for key, val in fixes_two.items():
        fixed_expr = fixed_expr.replace(key, val)
    fixed_expr = correct_expression(fixed_expr)
    return fixed_expr


def floats_handling(num: Any) -> Any:
    """Определяет нужно ли писать десятичную часть числа"""
    return num if num - int(num) else int(num)


def paranthesis_check(input_field):
    if input_field.count("(") != input_field.count(")"):
        return False
    return True


def check_before_del(input_field: str, funcs: tuple) -> int:
    """Определяет сколько символов нужно удалить во время команды CE"""
    quantity = -1
    for f in funcs:
        func = f[:-1]
        if input_field.endswith(func):
            quantity = -len(func)
            break

    if input_field.endswith("mod"):
        quantity = -3

    return quantity


def reverse_expression(input_field) -> str:
    """Разворачивает строку для Польской нотации"""
    exp = list(input_field[::-1])
    for i in range(len(exp)):
        if exp[i] == "(":
            exp[i] = ")"
        elif exp[i] == ")":
            exp[i] = "("
    return ''.join(exp)
