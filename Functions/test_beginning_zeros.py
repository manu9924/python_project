def beginning_zeros(a: str) -> int:
    b = int(a)
    if not b:
        return len(a)
    return len(a) - len(str(b))


def test_beginning_zeros():
    assert beginning_zeros('000356') == 3