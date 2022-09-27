def end_zeros(a: int) -> int:
    b = str(a)
    return len(b) - len(b.strip('0'))

def test_end_zeros():
    assert end_zeros(52300) == 2

