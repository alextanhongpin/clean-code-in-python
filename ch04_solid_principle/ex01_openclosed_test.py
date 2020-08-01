from .ex01_openclosed import SystemMonitor


def test_openclosed_1():
    l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    assert l1.identify_event().__class__.__name__ == "LoginEvent"

    l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    assert l2.identify_event().__class__.__name__ == "LogoutEvent"

    l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    assert l3.identify_event().__class__.__name__ == "UnknownEvent"
