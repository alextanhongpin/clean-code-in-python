"when the attribute of the object does not exists, python looks for the __getattr__ method"


class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "")
            return f"[fallback resolved] {name}"

        # IMPORTANT: Raise AttributeError, so that getattr(obj, attr,
        # default) will return the default value and not raise
        # Exception.
        raise AttributeError(f"{self.__class__.__name__} has no attribute {attr}")
