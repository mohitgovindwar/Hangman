import random

word_list = ['SHIELD', 'SHADOW', 'IS', 'WAS', 'BEFORE']


def getRandom():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = '_ ' * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
    tries = 6

    print('Lets play Hangman!')
    print(displayHangman(tries))
    print(word_completion)
    print('\n')

    while not guessed and tries > 0:
        guess = input('Enter your guess: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You have already guessed the letter', guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Good job,', guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_word:
                print('You already guessed the words', guess)
            elif guess != word:
                print(guess, 'is not the word.')
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word_completion = word


        else:
            print('Not a valid guess.')
        print(displayHangman(tries))
        print(word_completion)
        if guessed:
            print('Congrats,you guessed the word! You win')
        else:
            if tries == 0:
                print('Sorry,you ran out of tries. The word was ' + word + '.' + ' Maybe next time. ')

def displayHangman(tries):
    stages = [
        """
            --------
            |    |
            |    O
            |   \\|/
            |    |
            |   / \\
            -
        """,

        """
            --------
            |    |
            |    O
            |   \\|/
            |    |
            |   / 
            -
        """,

        """
            --------
            |    |
            |    O
            |   \\|/
            |    |
            |   
            -
        """,

        """
            --------
            |    |
            |    O
            |   \\|/
            |    
            |   
            -
        """,

        """
            --------
            |    |
            |    O
            |   \\|
            |    
            |   
            -
        """,

        """
            --------
            |    |
            |    O
            |   
            |    
            |   
            -
        """,

        """
            --------
            |    |
            |    
            |   
            |    
            |   
            -
        """
    ]
    return stages[tries]


def main():
    word = getRandom()
    play(word)

    while input('Do you want to play again(Y/N): ').upper() == 'Y':
        word = getRandom()
        play(word)

main()
