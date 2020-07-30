"module is awesome"


def main():
    "this is the main"
    hello("john")


def hello(name: str) -> str:
    "hello greets the given name"
    return f"hi, {name}"


if __name__ == "__main__":
    main()
