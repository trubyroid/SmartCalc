import pytest
# import allure


@pytest.mark.parametrize("expression, expected_result",
                         [("1024+4", 1028),
                          ("-203+-407", -610),
                          ("55-5", 50),
                          ("-7-3", -10),
                          ("40*60", 2400),
                          ("12345*0", 0),
                          ("0+0+0+0+1", 1),
                          ("-7--3", -4),
                          ("500/100", 5),
                          ("2**5", 32),
                          ("-7**5", -16807),
                          ("2+2*2", 6),
                          ("5*8+(3+3)", 46),
                          ("9%2%2", 1),
                          ("sqrt(4)", 2),
                          ("sqrt(256)", 16),
                          ("log(100) + log(10000)", 6),
                          ("+-11", -11),
                          ("+11", 11)])
def test_simple_operations(expression, expected_result, calc_model):
    assert calc_model.calculate_expression(expression) == expected_result


# @allure.description("""
# В рамках этих тест-кейсов разные машины могут давать разный результат.
# Причина в разных способах округления чисел с плавающей точкой.
# """)
@pytest.mark.xfail(condition=lambda: True, reason='expecting failure')
@pytest.mark.parametrize("expression, expected_result",
                         [("log(10) + log(10)", 4.605170185988092),
                          ("sin(4)", -0.7568024953079282),
                          ("cos(8)", -0.14550003380861354),
                          ("tan(5)", -3.380515006246585),
                          ("asin(0.5)", 0.5235987755982988),
                          ("acos(0.8)", 0.6435011087932843),
                          ("atan(0.9)", 0.7328151017865067)])
def test_trigonometry_operations(expression, expected_result, calc_model):
    assert calc_model.calculate_expression(expression) == expected_result
