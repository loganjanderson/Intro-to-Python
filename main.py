def guessing_game():
    while True:
        print('What animal am I thinking of?')
        guess = input()

        if guess == 'elephant':
            print('Great job!')
            return False
        else:
            print(f'No, {guess} is not correct. Try again\n')

guessing_game()