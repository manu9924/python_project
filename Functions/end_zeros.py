def end_zeros(a: int) -> int:
    b = str(a)
    return len(b) - len(b.strip('0'))