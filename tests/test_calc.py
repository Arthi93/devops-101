import pytest

def add(a,b):
    return a + b

def test_add():
    assert add(2, 3) == 5

@pytest.mark.parametrize("a,b,result",[
    (2, 5, 7),
    (-1, 1, 0),
    (-1, -18, -19)
])

def test_param_add(a,b,result):
    assert a + b == result

# def test_add2():
#     assert add(2, 3) == 6