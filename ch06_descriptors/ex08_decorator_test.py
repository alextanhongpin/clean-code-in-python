from datetime import date
from .ex08_decorator import LoginEvent


def test_login_event():
    evt = LoginEvent("john", "123456", "0.0.0.0", date(2020, 1, 1))
    assert evt.username == "john"
    assert evt.password == "**redacted**"
    assert evt.ip == "0.0.0.0"
    assert evt.timestamp == "2020-01-01 00:00"
