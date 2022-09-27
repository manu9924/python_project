def max_digit(a: int) -> int:
    a = str(a)
    a = max(map(int, str(a)))
    return a