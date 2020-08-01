from .ex05_generator_send import sequence


def test_send():
    seq = sequence()
    assert next(seq) == 0
    seq.send(2)
    assert next(seq) == 3
    assert next(seq) == 4
