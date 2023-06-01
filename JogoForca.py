import random

def hangman():
    words = ['python', 'programming', 'code', 'hangman', 'game']
    word = random.choice(words)
    guesses = ''
    turns = 6

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                failed += 1
        print()

        if failed == 0:
            print('Parabéns! Você acertou a palavra!')
            break

        guess = input('Digite uma letra: ')
        guesses += guess

        if guess not in word:
            turns -= 1
            print('Errado! Você tem mais', turns, 'tentativas.')

            if turns == 0:
                print('Game Over. A palavra era', word)

hangman()
