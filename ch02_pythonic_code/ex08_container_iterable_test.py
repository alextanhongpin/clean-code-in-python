from datetime import date
from .ex08_container_iterable import DateRangeContainerIterable


def test_date_range_container_iterable():
    r = DateRangeContainerIterable(date(2020, 1, 1), date(2020, 1, 7))
    assert (
        ", ".join(map(str, r))
        == "2020-01-01, 2020-01-02, 2020-01-03, 2020-01-04, 2020-01-05, 2020-01-06"
    )
    assert max(r) == date(2020, 1, 6)
