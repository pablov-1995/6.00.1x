"""
 Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences of the digit 7 in N.

For example:
count7(717) -> 2
count7(1237123) -> 1
count7(8989) -> 0

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).

This function has to be recursive; you may not use loops! This function takes in one integer and returns one integer.
"""
def count7(N):
    '''
    N: a non-negative integer
    '''
    # Your code here
    if N//10 == 0:
        if N == 7:
            return 1
        else:
            return 0
    else:
        if N%10 == 7:
            return count7(N//10) + 1
        else:
            return count7(N//10)