"""


Implement a function that meets the specifications below.

def sum_digits(s):
    ...

For example, sum_digits("a;35d4") returns 12.

"""

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    digs = [c for c in s.split() if c.isdigit()]
    if not len(digs):
        raise ValueError
    else:
        return sum(digs)