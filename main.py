import random

max_gueses = 10
max_numbers = 3

def main():
    print(f'''

I am thinking of a {max_numbers}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
          

When I say:    That means:
  Dash         One digit is correct but in the wrong position.
  Point        One digit is correct and in the right position.
  Bagels       No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Point Dash.''')

    while True:  
        secretnum = getsecretnum()
        print('I have thought up a number.')
        print(f'You have {max_gueses} guesses to get it.')

        numguesses = 1
        while numguesses <= max_gueses:
            guess = ''
            while len(guess) != max_numbers or not guess.isdecimal():
                print(f"Guess #{numguesses}")
                guess = input('Guess the number: ')

            clues = getclues(guess, secretnum)
            print(clues)

            numguesses += 1

            if guess == secretnum:
                break 

        if guess == secretnum:
            print("You guessed it!")
        else:
            print('You ran out of guesses.')
            print(f'The answer was {secretnum}.')

        
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break

    print('Thanks for playing!')  


def getsecretnum():
    numbers = list('123456789')  
    random.shuffle(numbers)

    num = ''
    for i in range(max_numbers):
        num += str(numbers[i])
    return num

def getclues(guess, secretnum):
    if guess == secretnum:
        return "You got it"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretnum[i]:
            clues.append("Point")
        elif guess[i] in secretnum:
            clues.append("Dash")

    
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()
