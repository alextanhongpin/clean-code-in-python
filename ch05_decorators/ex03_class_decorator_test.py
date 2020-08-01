import datetime
from .ex03_class_decorator import LoginEvent


def test_decorator_serialization():
    serialized = LoginEvent(
        "john", "123456", "0.0.0.0", datetime.date(2020, 1, 1)
    ).serialize()
    assert serialized["username"] == "john"
    assert serialized["password"] == "**redacted**"
    assert serialized["ip"] == "0.0.0.0"
    assert serialized["timestamp"] == "2020-01-01 00:00"
