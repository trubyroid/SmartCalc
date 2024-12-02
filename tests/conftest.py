import pytest
import allure
from ..smartcalc.model.model import Model


@pytest.fixture(scope="session")
@allure.title("Создание инстанса класса Model")
def calc_model():
    return Model()
