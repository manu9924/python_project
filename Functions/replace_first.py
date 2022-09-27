from typing import Iterable


def replace_first(items: list) -> Iterable:
    if items:
        items.append(items.pop(0))
    return items