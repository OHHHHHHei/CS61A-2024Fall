
from operator import floordiv, mod

def divide_exact(n, d):
    """Return the quotient and remainder of n divided by d.
    
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    return floordiv(n, d), mod(n, d)

def absolute_value(x):
    """Return the absolute value of x.
    
    >>> absolute_value(-5)
    5
    >>> absolute_value(5)
    5
    """
    if x < 0:
        return -x
    else:
        return x