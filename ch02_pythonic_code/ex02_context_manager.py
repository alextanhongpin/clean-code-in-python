def stop_database():
    print("stopping database")


def start_database():
    print("starting database")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # This will always be called even if an exception occurs.
        print(exc_type, exc_value, exc_traceback)
        start_database()


def db_backup():
    print("running backup")


def main():
    with DBHandler():
        raise Exception("hello world")
        db_backup()


if __name__ == "__main__":
    main()
