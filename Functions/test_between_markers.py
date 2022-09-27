def between_markers(text: str, start: str, end: str) -> str:
    return text[(text.index(start)+1):text.index(end)]

def test_between_markers():
    assert between_markers('find the <word> inside the markers', '<', '>') == 'word'
