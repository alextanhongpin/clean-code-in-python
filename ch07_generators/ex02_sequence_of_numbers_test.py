from .ex02_sequence_of_numbers import SequenceOfNumbers


def test_sequence_of_numbers():
    seq = SequenceOfNumbers()
    assert next(seq) == 0
    assert next(seq) == 1


def test_enumerate_sequence_of_numbers():
    seq = list(zip(SequenceOfNumbers(), "abcde"))
    assert seq == [(0, "a"), (1, "b"), (2, "c"), (3, "d"), (4, "e")]
