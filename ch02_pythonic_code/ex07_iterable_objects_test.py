import pytest
from datetime import date
from .ex07_iterable_objects import DateRangeIterable


def test_date_range_iterable():
    r = DateRangeIterable(date(2020, 1, 1), date(2020, 1, 7))
    assert next(r) == date(2020, 1, 1)
    assert next(r) == date(2020, 1, 2)
    assert next(r) == date(2020, 1, 3)
    assert next(r) == date(2020, 1, 4)
    assert next(r) == date(2020, 1, 5)
    assert next(r) == date(2020, 1, 6)
    pytest.raises(StopIteration, next, r)
