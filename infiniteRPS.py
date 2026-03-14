import random,sys

wins = 0
losses = 0
ties = 0

print('ROCK PAPER SCISSORS')
print('%s Wins %s Losses %s Ties' %(wins, losses, ties))

while True :
    print('Enter your move : (r)ock (p)aper (s)cissors or (quit)')
    uMove = input()
    if uMove == 'q':
        sys.exit()
    if uMove == 'r' or uMove =='p' or uMove =='s':
        if uMove == 'r':
            print('ROCK vs ___')
        elif uMove == 'p':
            print('PAPER vs ___')
        elif uMove == 's':
            print('SCISSORS vs ___')

        ranNum = random.randint(1,3)
        if ranNum == 1:
            cMove = 'r'
            print('ROCK')
        elif ranNum == 2:
            cMove = 'p'
            print('PAPER')
        elif ranNum == 3:
            cMove = 's'
            print('SCISSORS')



        if uMove == cMove :
            print('Its a tie!')
            ties = ties + 1
        elif uMove == 'r' and cMove == 's':
            print('YOU WON!')
            wins = wins + 1
        elif uMove == 'p' and cMove == 'r':
            print('YOU WON!')
            wins = wins + 1
        elif uMove == 's' and cMove == 'p':
            print('YOU WON!')
            wins = wins + 1
        elif uMove == 'r' and cMove == 'p':
            print('YOU LOSE!')
            losses = losses + 1
        elif uMove == 'p' and cMove == 's':
            print('YOU LOSE!')
            losses = losses + 1
        elif uMove == 's' and cMove == 'r':
            print('YOU LOSE!')
            losses = losses + 1
    else :
        print('Type one of r, p, s or q')


