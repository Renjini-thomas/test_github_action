from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(1,2)==3

def test_sub():
    assert sub(4,2)==2
    assert sub(9,8)==1
    assert sub(7,4)==3
