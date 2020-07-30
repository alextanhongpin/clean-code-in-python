from .ex12_callable_objects import CallCount


def test_call_count():
    cc = CallCount()
    assert cc(1) == 1
    assert cc(1) == 2
    assert cc(2) == 1

    cc2 = CallCount()
    assert cc2(1) == 1
    assert cc2(2) == 1
