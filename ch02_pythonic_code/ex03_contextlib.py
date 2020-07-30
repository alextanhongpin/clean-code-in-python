"contextlib converts a generator function into a context manager"
import contextlib


def stop_database():
    print("stopping database")


def start_database():
    print("starting database")


def db_backup():
    print("running backup")


@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()


def main():
    with db_handler():
        db_backup()


if __name__ == "__main__":
    main()
