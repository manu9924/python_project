def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    return elements[0], elements[2],elements[-2]

def test_easy_unpack():
    assert easy_unpack([2,4,5,8,7,6,4,5,7]) == (2,5,5)
