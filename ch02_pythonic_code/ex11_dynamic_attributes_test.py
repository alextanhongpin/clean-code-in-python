import pytest
from .ex11_dynamic_attributes import DynamicAttributes


def test_dynamic_attributes():
    attr = DynamicAttributes("hello")
    assert attr.attribute == "hello"
    assert attr.fallback_name == "[fallback resolved] name"
    assert attr.fallback_age == "[fallback resolved] age"
    with pytest.raises(AttributeError):
        attr.random_attribute

    attr.__dict__["fallback_new"] = "new"
    assert attr.fallback_new == "new"
    assert getattr(attr, "something", "default") == "default"
    assert getattr(attr, "something", 1234) == 1234
