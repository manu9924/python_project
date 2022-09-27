from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        return items[items.index(border):]
    else:
        return items
    
def test_remove_all_before():
    assert remove_all_before([1, 1, 2, 4, 2, 3, 4], 2) == [2, 4, 2, 3, 4]