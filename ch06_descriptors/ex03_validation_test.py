import pytest
from .ex03_validation import ClientClass


def test_validation():
    cls = ClientClass()
    cls.descriptor = 42
    assert cls.descriptor == 42

    with pytest.raises(ValueError):
        cls.descriptor = -42
