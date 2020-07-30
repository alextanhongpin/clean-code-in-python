from datetime import date
from .ex09_sequences import DateRangeSequence


def test_date_range_sequence():
    seq = DateRangeSequence(date(2020, 1, 1), date(2020, 1, 7))
    assert len(seq) == 6
    assert seq[0] == date(2020, 1, 1)
    assert seq[-1] == date(2020, 1, 6)
