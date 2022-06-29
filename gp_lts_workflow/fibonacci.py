"""
Every good ccientist needs doubly recursive fibonacci numbers
"""


def fibonacci(n: int) -> int:
    '''
    Calculate the nth fibonacci number.

    Parameters
    ----------
    n : int
        Which fibonacci number to compute

    Returns
    -------
    fib_n : int
        the nth fibonacci number
    '''
    if n < 0:
        raise ValueError(f'n must be >= 0, got {n}')

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
