"""
 Write a function that satisfies the following docstring:

def largest_odd_times(L):
    ...

For example, if

    largest_odd_times([2,2,4,4]) returns None
    largest_odd_times([3,9,5,3,5,3]) returns 9

"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number
        of times in L. If no such element exists, returns None """
    # Your code here
    odd_count = [i for i in L if L.count(i) % 2]
    if len(odd_count):
        return max(odd_count)
    else:
        return None