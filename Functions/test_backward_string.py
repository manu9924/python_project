def backward_string(val: str) -> str:
   
    return val[::-1]

def test_backward_string():
    assert backward_string('test') == 'tset'
    