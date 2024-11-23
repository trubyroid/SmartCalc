import pytest
from ..smartcalc.model.model import Model


@pytest.fixture(scope="session")
def calc_model():
    return Model()
