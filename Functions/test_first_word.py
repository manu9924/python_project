def first_word(text: str) -> str:
     words = text.split()
     return words[0]

def test_first_word():
    assert first_word('Word is the first word') == 'Word'
    