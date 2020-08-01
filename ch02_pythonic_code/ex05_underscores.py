class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60

        # Name mangling, python converts this to _<class-name>__<attribute-name>
        # NOTE: Do not use double underscore, a.k.a (dunder, double underscore).
        self.__hidden = False
