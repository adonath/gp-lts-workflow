import astropy.unit as u
from example_subpkg import Square

def test_square():
    square = Square(1*u.m, 1*u.m)
    area = square.area

    assert area.to_value("cm2") == 10000

