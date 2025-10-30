from cube import CubeObject
from pytest import raises

def test_valid_init():
    cube = CubeObject(0.5, 1, -1)
    assert cube.side == 0.5
    assert cube.x == 1
    assert cube.y == -1

def test_negative_value_side_init_fails():
    with raises(ValueError):
        CubeObject(-1, -1, 1)

def test_out_of_bounds_fails():
    with raises(ValueError):
        CubeObject(1, 11, -11)

def test_string_in_init_fails():
    with raises(TypeError):
        CubeObject("1", "1", "1")

def test_empty_init_fails():
    with raises(TypeError):
        CubeObject()

def test_bool_in_init_fails():
    with raises(TypeError):
        CubeObject(True, False, True)