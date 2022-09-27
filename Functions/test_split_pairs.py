from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    if len(text) % 2:
        text += '_'
    result = []
    while text:
        result.append(text[:2])
        text = text[2:]
    return result

def test_split_pairs():
    assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]