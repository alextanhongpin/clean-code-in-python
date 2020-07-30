from .ex05_underscores import Connector


def test_connector():
    conn = Connector("postgresql://localhost")
    assert conn.source == "postgresql://localhost"
    assert conn._timeout == 60
    assert conn.__dict__.get("_timeout") == 60
    assert conn.__dict__.get("__hidden") is None
    assert conn.__dict__.get("_Connector__hidden") == False
