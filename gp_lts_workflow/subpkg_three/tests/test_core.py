from .. import square
from numpy.testing import assert_allclose, assert


def test_square():
    assert_allclose(square(-2.5), 6.25)
    assert square(3) == 9
