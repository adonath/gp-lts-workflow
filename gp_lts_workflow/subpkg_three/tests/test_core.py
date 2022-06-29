from .. import *
from numpy.testing import assert_allclose

def test_square():
    assert_allclose(square(-3), 9)

