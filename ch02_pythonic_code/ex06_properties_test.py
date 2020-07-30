import pytest
from .ex06_properties import User


def test_user():
    john = User("john")
    john.email = "john.doe@mail.com"
    assert john.email == "john.doe@mail.com"
    with pytest.raises(ValueError):
        john.email = "john@"
