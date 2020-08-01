from .ex06_yield_from import naive_chain, chain


def execute(ch):
    nc = ch([1, 2,], "hi", ("tuple", "of", "values"))
    assert next(nc) == 1
    assert next(nc) == 2
    assert next(nc) == "h"
    assert next(nc) == "i"
    assert next(nc) == "tuple"
    assert next(nc) == "of"
    assert next(nc) == "values"


def test_chain():
    execute(naive_chain)
    execute(chain)
