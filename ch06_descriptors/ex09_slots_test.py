import pytest
from .ex09_slots import Coordinate2D


def test_slots():
    zero = Coordinate2D(0, 0)
    zero.lat = 100
    zero.long = 99

    assert zero.lat == 100
    assert zero.long == 99
    with pytest.raises(AttributeError):
        zero.name = "latlng"
