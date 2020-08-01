from .ex08_decorator_class import inject_db_driver


@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")


def test_function_decorator():
    assert run_query("test_driver") == "query test_function at test_driver"


class DataHandler:
    @inject_db_driver
    def run_query(self, driver):
        return driver.execute(self.__class__.__name__)


def test_class_decorator():
    dh = DataHandler()
    assert dh.run_query("test_driver") == "query DataHandler at test_driver"
