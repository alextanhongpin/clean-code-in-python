import pytest
from .ex01_number_sequence import NumberSequence


def test_number_sequence():
    seq = NumberSequence()
    assert seq.next() == 0
    assert seq.next() == 1

    seq = NumberSequence(10)
    assert seq.next() == 10
    assert seq.next() == 11


def test_enumerate_number_sequence():
    with pytest.raises(TypeError):
        list(zip(NumberSequence(), "abcde"))
