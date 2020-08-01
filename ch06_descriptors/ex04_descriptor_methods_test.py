import pytest
from .ex04_descriptor_methods import User


def test_user_permissions():
    admin = User("john", "john.doe@mail.com", ["admin"])
    del admin.email
    assert admin.email is None

    alice = User("alice", "alice@mail.com")
    with pytest.raises(ValueError):
        del alice.email

    with pytest.raises(ValueError):
        alice.email = None
