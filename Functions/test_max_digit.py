def max_digit(a: int) -> int:
    a = str(a)
    a = max(map(int, str(a)))
    return a

def test_max_digit():
    assert max_digit(675980) == 9
