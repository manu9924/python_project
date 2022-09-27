from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        return items[items.index(border):]
    else:
        return items