from rectangle import RectangleObject
from pytest import raises

def test_valid_init():
    rectangle = RectangleObject(0.5, 1, -1, 1)
    assert rectangle.width == 0.5
    assert rectangle.height == 1
    assert rectangle.x == -1
    assert rectangle.y == 1

def test_negative_value_width_height_init_fails():
    with raises(ValueError):
        RectangleObject(-1, -1, 1, 1)

def test_out_of_bounds_fails():
    with raises(ValueError):
        RectangleObject(1, 1, 11, -11)

def test_string_in_init_fails():
    with raises(TypeError):
        RectangleObject("1", "1", "1", "1")

def test_empty_init_fails():
    with raises(TypeError):
        RectangleObject()

def test_bool_in_init_fails():
    with raises(TypeError):
        RectangleObject(True, True, False, True)