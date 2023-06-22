from ..model.model import CalculatorModel
import pytest

calc_model = CalculatorModel()


@pytest.mark.parametrize("case, expected_exception",
                         [("15/0", ZeroDivisionError),
                          ("0+00123", SyntaxError),
                          ("sqrt(-1)", ValueError),
                          ("()*()*()*0", TypeError)])
def test_negative_cases(monkeypatch, case, expected_exception):

    def mock_set_error_to_entry(*args, **kwargs):
        print("I'm here")

    monkeypatch.setattr("src.model.model.CalculatorModel.set_error_to_entry",
                        mock_set_error_to_entry)

    with pytest.raises(expected_exception):
        calc_model.calculate_expression(case)