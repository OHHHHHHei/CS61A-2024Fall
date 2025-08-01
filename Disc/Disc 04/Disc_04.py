def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    # if the m or n equal to 1
    if m == 1:
        return 1
    if n == 1:
        return 1
    
    # go upper or go right is equivalent to reducing the vertical or horizontal axis of the entire grid
    # go upper add go right
    return paths(m - 1, n) + paths(m, n - 1)

def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    if len(s) == 0: # base case
        return 1
    if len(s) == 1: # base case
        return s[0]
    # use the first number
    use_first = s[0] * max_product(list(s[i] for i in range(2, len(s))))
    # skip the first number
    use_second = max_product(list(s[i] for i in range(1, len(s))))
    # return the maximum of those two ways
    return max(use_first, use_second)

def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1): # the start number
        # sums(n - k, m) recursion to construct lists that sum to n by putting a k on the front.
        # avoid the k equals to the first element of rest
        result = result + [[k] + rest for rest in sums(n - k, m) if rest == [] or k != rest[0]]
    return result
