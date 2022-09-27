def beginning_zeros(a: str) -> int:
    b = int(a)
    if not b:
        return len(a)
    return len(a) - len(str(b))