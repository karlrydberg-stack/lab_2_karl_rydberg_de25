from circle import CircleObject
from pytest import raises

def test_valid_init():
    circle = CircleObject(0.5, -1, 1)
    assert circle.radius == 0.5
    assert circle.x == -1
    assert circle.y == 1

def test_value_radius_init_fails():
    with raises(ValueError):
        CircleObject(0, 1, 1)

def test_out_of_bounds_fails():
    with raises(ValueError):
        CircleObject(1, 11, 11)

def test_string_in_init_fails():
    with raises(TypeError):
        CircleObject("1", "1", "1")

def test_empty_init_fails():
    with raises(TypeError):
        CircleObject()

def test_bool_in_init_fails():
    with raises(TypeError):
        CircleObject(True, True, True)

def test_circle_area_valid():
    circle = CircleObject(1, 1, 1)
    expected_area = 1 * 1 * 3.14
    assert circle.area_ == expected_area

def test_circle_area_fails():
    circle = CircleObject(2, 1, 1)
    unexpected_area = 1 * 1 * 3.14
    assert circle.area_ != unexpected_area