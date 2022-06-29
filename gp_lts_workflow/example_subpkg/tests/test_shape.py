import astropy.unit as u
from example_subpkg import Rectangle

def test_rectangle():
    rectangle = Rectangle(1*u.m, 1*u.m)
    area = rectangle.area

    assert area.to_value("cm2") == 10000

