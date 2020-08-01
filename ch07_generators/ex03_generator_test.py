from .ex03_generator import sequence


def test_sequence_generator():
    seq = sequence()
    assert next(seq) == 0
    assert next(seq) == 1
