from .ex01_mixins import BaseTokenizer, Tokenizer


def test_base_tokenizer():
    tk = BaseTokenizer("some-random-slug")
    assert list(tk) == ["some", "random", "slug"]


def test_mixin_tokenizer():
    tk = Tokenizer("some-random-slug")
    assert list(tk) == ["SOME", "RANDOM", "SLUG"]
    assert [cls.__name__ for cls in Tokenizer.mro()] == [
        "Tokenizer",
        "UpperIterableMixin",
        "BaseTokenizer",
        "object",
    ]
