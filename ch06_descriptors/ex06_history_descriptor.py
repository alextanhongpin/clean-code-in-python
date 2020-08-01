class HistoryTracedAttribute:
    def __init__(self, trace_attribute_name) -> None:
        self.trace_attribute_name = trace_attribute_name
        self._name = None

    def __set_name__(self, instance, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        self._set_default(instance, value)
        if self._needs_to_track_change(instance, value):
            instance.__dict__[self.trace_attribute_name].append(value)
        instance.__dict__[self._name] = value

    def _set_default(self, instance, value):
        instance.__dict__.setdefault(self.trace_attribute_name, [])

    def _needs_to_track_change(self, instance, value):
        try:
            current_value = instance.__dict__[self._name]
        except KeyError:
            return True
        return value != current_value


class Traveller:
    current_city = HistoryTracedAttribute("cities_visited")

    def __init__(self, name, current_city):
        self.name = name
        self.current_city = current_city
