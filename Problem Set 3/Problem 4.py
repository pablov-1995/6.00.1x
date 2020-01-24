"""
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.
"""


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    numletters = len(secretWord)
    defaultGuesses = 8
    avletters = 'abcdefghijklmnopqrstuvwxyz'
    lg = []
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', numletters, ' letters long.')
    while not isWordGuessed(secretWord, lg):
        print('-------------')
        print('You have ', defaultGuesses, ' left.')
        print('Available letters: ' + avletters)
        guess = input('Please guess a letter: ').lower()
        if guess in lg:
            print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lg))
        else:
            lg.append(guess)
            avletters = getAvailableLetters(lg)
            if guess in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, lg))
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lg))
                defaultGuesses -= 1
                if defaultGuesses == 0:
                    print('-------------')
                    print('Sorry, you ran out of guesses. The word was ' + secretWord)
                    return None

    print('-------------')
    print('Congratulations, you won!')