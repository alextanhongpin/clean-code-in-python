import pytest
from .ex01_decorator import retry


@retry
def run_operation(task: str) -> str:
    if task.isdigit():
        return f"run {task}"
    raise ValueError("not a digit")


def test_retry():
    assert run_operation("1") == "run 1"
    assert run_operation("10") == "run 10"
    pytest.raises(ValueError, run_operation, "xyz")
