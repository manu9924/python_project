def number_length(a: int) -> int:
    a = str(a)
    res = len(a)
    return res

def test_number_length():
    assert number_length(589624) == 6