from ..model.model import CalculatorModel
import pytest

calc_model = CalculatorModel()


@pytest.mark.parametrize("expression, expected_result",
                         [(["11", "5", "6", "+", "-"], 0),
                          (["2", "(", "4", "5", "+", ")", "*"], 18),
                          (["9", "(", "(", "6", "2", "2", 
                            "**", "-", ")", ")", "%"], 1),
                          (["11", "-"], -11),
                          (["+11", "-"], -11),
                          (["11", "+"], 11),
                          (["-11", "+"], -11)])
def test_polish_notation(expression, expected_result):
    assert calc_model.polish_calculate(expression) == expected_result
