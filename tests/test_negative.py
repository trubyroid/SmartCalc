from ..model.model import CalculatorModel
import pytest

calc_model = CalculatorModel()


@pytest.mark.parametrize("case, expected_exception",
                         [("15/0", ZeroDivisionError),
                          ("0+00123", SyntaxError),
                          ("sqrt(-1)", ValueError),
                          ("()*()*()*0", TypeError)])
def test_negative_cases(monkeypatch, case, expected_exception):

    with pytest.raises(expected_exception):
        calc_model.get_result(case)
