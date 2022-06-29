import pytest
import astropy.units as u
from ..shape import Rectangle


def test_rectangle():
    rectangle = Rectangle(1 * u.m, 1 * u.m)
    area = rectangle.area

    assert area.to_value("cm2") == 10000


def test_unit_rectangle():
    with pytest.raises(u.UnitsError):
        Rectangle(1 * u.s, 1 * u.m)
