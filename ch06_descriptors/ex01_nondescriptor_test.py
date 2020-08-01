from .ex01_nondescriptor import Client


def test_non_descriptor():
    assert Client().attribute.value == 42
