def most_frequent(data: list[str]) -> str:
    return max(data, key=data.count)

def test_most_frequent():
    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
    
