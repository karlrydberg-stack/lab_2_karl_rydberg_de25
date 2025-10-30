from sphere import SphereObject
from pytest import raises

def test_valid_init():
    sphere = SphereObject(0.5, -1, 1)
    assert sphere.radius == 0.5
    assert sphere.x == -1
    assert sphere.y == 1

def test_value_radius_init_fails():
    with raises(ValueError):
        SphereObject(0, 1, 1)

def test_out_of_bounds_fails():
    with raises(ValueError):
        SphereObject(1, 11, 11)

def test_string_in_init_fails():
    with raises(TypeError):
        SphereObject("1", "1", "1")

def test_empty_init_fails():
    with raises(TypeError):
        SphereObject()
def test_bool_in_init_fails():
    with raises(TypeError):
        SphereObject(True, True, True)