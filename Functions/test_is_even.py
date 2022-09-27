def is_even(num: int) -> bool:
    if not num % 2:
        return True
    else:
        return False

def test_is_even():
    assert is_even(46) == True