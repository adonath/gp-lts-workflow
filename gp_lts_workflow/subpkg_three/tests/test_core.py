from .. import square
from numpy.testing import assert_allclose


def test_square():
    assert_allclose(square(-2.5), 6.25)
    assert square(3) == 9
