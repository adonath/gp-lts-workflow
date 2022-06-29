import pytest


NUMBERS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]


@pytest.mark.parametrize('n,expected', enumerate(NUMBERS))
def test_fibonacci(n, expected):
    from gp_lts_workflow.fibonacci import fibonacci

    assert fibonacci(n) == expected
