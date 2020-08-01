"""The solution to the previous issue - implement the decorator as a
class object and make this object a description, by implementing the
__get__ method."""


from functools import wraps
from types import MethodType


class DBDriver:
    def __init__(self, dbstring):
        self.dbstring = dbstring

    def execute(self, query):
        return f"query {query} at {self.dbstring}"


class inject_db_driver:
    """Convert a string to a DBDriver instance and pass this to the wrapped function."""

    def __init__(self, function):
        self.function = function
        wraps(self.function)(self)

    def __call__(self, dbstring):
        return self.function(DBDriver(dbstring))

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.__class__(MethodType(self.function, instance))
