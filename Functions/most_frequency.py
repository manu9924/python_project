def most_frequent(data: list[str]) -> str:
    return max(data, key=data.count)