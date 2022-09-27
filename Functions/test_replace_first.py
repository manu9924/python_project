from typing import Iterable


def replace_first(items: list) -> Iterable:
    if items:
        items.append(items.pop(0))
    return items

def test_replace_first():
    assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
    