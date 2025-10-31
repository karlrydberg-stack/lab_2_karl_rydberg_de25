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

def test_rectangle_area_valid():
    rectangle = RectangleObject(1, 3, 1, 4)
    expected_area = 1 * 3
    assert rectangle.area_ == expected_area

def test_rectangle_area_fails():
    rectangle = RectangleObject(2, 1, 1, 5)
    unexpected_area = 1 * 9 * 2
    assert rectangle.area_ != unexpected_area