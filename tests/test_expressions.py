import pytest

@pytest.mark.parametrize("expression, expected_result",
                         [("(((4+5)*(8-2)*(3**2))+3)*2", 978),
                          ("((((4+5))))-2", 7),
                          ("4**2*5/8+5-5%sqrt(4)", 14)])
def test_expressions(expression, expected_result, calc_model):
    assert calc_model.calculate_expression(expression) == expected_result
