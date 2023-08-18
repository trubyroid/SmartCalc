"""
В этом модуле находится класс окна помощи.
"""

from tkinter import ttk


class CalculatorHelp:
    def __init__(self):
        self.tk_window = None
        self._name = "Help"
        self._geometry = "490x480+200+200"
        self._text = """
                РУКОВОДСТВО ПОЛЬЗОВАТЕЛЯ:\n
                Все стандартные функции работают как обычно.\n
                Введите выражение и нажмите \"=\".\n\n
                При переходе между режимами поле ввода очищается.\n
                Для работы в режиме польской нотации нажмите \"PN\".\n
                Для работы в режиме обратной польской нотации нажмите \"RPN\".\n
                В этих режимах все символы нужно будет разделять пробелами.\n
                В этих режимах запись в историю не производится.\n
                Для того чтобы вернуться в обычный режим нажмите \"Default\".\n\n
                Для того чтобы воспользоваться историей нажмите \"H\".\n
                Для построения графика введите функцию и нажмите \"F(x)\".\n\n
                Благодарю за интерес к моей работе.\n
                Успехов!
                """

    @property
    def name(self) -> str:
        return self._name

    @property
    def geometry(self) -> str:
        return self._geometry

    @property
    def text(self) -> str:
        return self._text

    def create_gui(self) -> None:
        label = ttk.Label(self.tk_window)
        label["text"] = self.text
        label.pack()
