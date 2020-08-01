import pytest
from .ex07_decorator import inject_db_driver


@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")


def test_function_decorator():
    assert (
        run_query("postgresql://localhost")
        == "query test_function at postgresql://localhost"
    )


class DataHandler:
    @inject_db_driver
    def run_query(self, driver):
        """this decorator will fail, because the method for class is declared with an additiona parameter self."""
        return driver.execute(self.__class__.__name__)


def test_class_decorator():
    dh = DataHandler()
    with pytest.raises(TypeError):
        dh.run_query("test_fails")
