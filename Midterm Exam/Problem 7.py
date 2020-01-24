"""
Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:

def satisfiesF(L):
    ...

For your own testing of satisfiesF, for example, see the following test function f and test code:

def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)

Should print:

2
['a', 'a']
"""


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    i = 0
    while i < len(L):
        if not f(L[i]):
            L.remove(L[i])
        else:
            i += 1
    return len(L)

run_satisfiesF(L, satisfiesF)