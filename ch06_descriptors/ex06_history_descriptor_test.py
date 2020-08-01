from .ex06_history_descriptor import Traveller


def test_traveller():
    t = Traveller("john", "Singapore")
    t.current_city = "Malaysia"

    assert t.cities_visited == ["Singapore", "Malaysia"]
    t.current_city = "Singapore"
    assert t.cities_visited == ["Singapore", "Malaysia", "Singapore"]
    t.current_city = "Singapore"
    assert t.cities_visited == [
        "Singapore",
        "Malaysia",
        "Singapore",
    ]
