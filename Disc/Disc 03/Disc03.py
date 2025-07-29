def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        print(n % 10)
        swipe(n // 10) # go down
        print(n % 10) # go up

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def f(i):
        if i >= n: # no factor between i and n, it is a prime number
            return True
        elif n % i == 0: # if there is a factor between i and n, then it is not be a prime number
            return False
        else:
            return f(i + 1) # recursive
    return f(2) # call the inner function
    
def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n): # if it is even, make a recursion and add one more than the rest of the length
    return hailstone(n // 2) + 1

def odd(n):# if it is odd, make clear if it is a base case
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        return hailstone(3 * n + 1) + 1


def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n - 2 <= 0:# the base case
        return n
    else:
        return n * skip_factorial(n - 2)
    

def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    def f(i, who, direction):
        if i == n: # base case
            return who
        "*** YOUR CODE HERE ***"
        if has_seven(i) or i % 7 == 0: # change the direction
            direction = -direction

        who += direction # next player

        if who > k: # keep in range
            who -= k
        if who < 1:
            who += k

        return f(i + 1, who, direction) # recursion

    return f(1, 1, 1) # call the function

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)

# write any code you want
from karel.stanfordkarel import *
def turn_around():
    turn_left()
    turn_left()

def move_back():
    turn_around()
    move()
    turn_around()

def find_middle_recursive():
    if front_is_clear():
        move()
        if front_is_clear():
            move()
            find_middle_recursive()
            move_back()

def main():
    find_middle_recursive()