import contextlib


def stop_database():
    print("stopping database")


def start_database():
    print("starting database")


class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, ext_type, ext_value, ext_traceback):
        start_database()


@dbhandler_decorator()
def db_backup():
    print("running backup")


def main():
    db_backup()


if __name__ == "__main__":
    main()
