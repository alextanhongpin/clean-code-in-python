import pytest
from .ex01_custom_sequences import Items


def test_custom_sequence():
    items = Items(1, 2, 3, 4, 5)
    assert items[0:2] == [1, 2]
    assert items[:1] == [1]
    assert items[2:4] == [3, 4]
