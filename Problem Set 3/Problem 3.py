"""
 Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz

Note that this function should return the letters in alphabetical order, as in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.
"""
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    returnlist = list('abcdefghijklmnopqrstuvwxyz')
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in returnlist:
            returnlist.remove(lettersGuessed[i])
    returnstr = ''.join(returnlist)
    return returnstr
