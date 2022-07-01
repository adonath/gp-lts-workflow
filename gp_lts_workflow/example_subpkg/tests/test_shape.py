import pytest
from numpy.testing import assert_allclose
import astropy.units as u
from ..shape import Rectangle, Circle


def test_rectangle():
    rectangle = Rectangle(1 * u.m, 1 * u.m)
    area = rectangle.area

    assert area.to_value("cm2") == 10000


def test_unit_rectangle():
    with pytest.raises(u.UnitsError):
        Rectangle(1 * u.s, 1 * u.m)
    with pytest.raises(ValueError):
        Rectangle(-1 * u.m, 1 * u.m)

def test_circle():
    circle = Circle(1 * u.m)
    area = circle.area

    assert_allclose(area.to_value("cm2"), 31456)
