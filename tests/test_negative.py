import pytest


@pytest.mark.parametrize("case, expected_exception",
                         [("15/0", ZeroDivisionError),
                          ("0+00123", SyntaxError)])
def test_negative_cases(monkeypatch, case, expected_exception, calc_model):

    with pytest.raises(expected_exception):
        calc_model.get_result(case)
