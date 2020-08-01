from .ex03_orthogonality import str_final_price, show_price


def test_str_final_price():
    assert str_final_price(10, 0.2, 0.5) == "6.0"
    assert str_final_price(10, 0.2, 0.5, fmt_function=show_price) == "$ 6.00"
