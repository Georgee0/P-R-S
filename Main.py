
# Rock, Paper and Scissors
import random, sys
print('ROCK PAPER SCISSORS')
wins = 0
losses = 0
ties = 0
while True:     # main game loop
    print('%s wins, %s losse, %s ties' %(wins, losses, ties))
    while True:     # player loop
        print('Enter move: (r)ock (p)aper (s)cissors (q)uit ')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        elif playerMove == 'r'  or playerMove == 'p' or playerMove == 's':
            break
        print('Type either r, p, s or q')
        # DISPLAY PLAYER INPUTS
    if playerMove == 'r':
        print('ROCK versus........')
    elif playerMove == 'p':
        print('PAPER versus.......')
    elif playerMove == 's':
        print('SCISSORS versus.......')
        # DISPLAY COMPUTER MOVES
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

   # RECORD FOR WINS, LOSSES OR TIES
        if playerMove == computerMove:
            print('it\'s a ties!')
            ties = ties + 1
        elif playerMove == 'r' and computerMove == 's':
            print(' YOu win!')
            wins = wins + 1
        elif playerMove == 'p' and computerMove == 'r':
            print('You win!')
            wins = wins + 1
        elif playerMove == 's' and computerMove == 'p':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'r' and computerMove == 'p':
            print(' You loss!')
            losses = losses + 1
        elif playerMove == 's' and computerMove == 'r':
            print('You loss!')
            losses = losses + 1
        elif playerMove == 'p' and computerMove == 's':
            print('You loss!')
            losses = losses + 1
            