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