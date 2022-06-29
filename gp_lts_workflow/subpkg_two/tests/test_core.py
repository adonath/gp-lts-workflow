from ..core import print_sum
import pytest

@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_print_sum(x, y):
    """the print sum should just return true"""
    assert print_sum(x, y)
