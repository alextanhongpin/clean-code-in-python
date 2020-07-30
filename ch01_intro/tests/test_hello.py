def hello(name: str) -> str:
    "hello greets the given name"
    return f"hi, {name}"


def test_greet():
    assert hello("john") == "hi, john"
