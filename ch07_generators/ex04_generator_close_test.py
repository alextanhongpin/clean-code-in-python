import pytest
from .ex04_generator_close import sequence


def test_close_generator():
    seq = sequence()
    assert next(seq) == 0
    seq.close()
    with pytest.raises(StopIteration):
        next(seq)
