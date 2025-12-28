from src.logic import check_even_odd, multiply

def test_check_even_odd():
    assert check_even_odd(2) == "Even"
    assert check_even_odd(3) == "Odd"

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5