import random,sys
RanNum = random.randint(1,20)
print('I am thinking of a number between 1 to 20')

for GuessTook in range(5) :
    print('Take a guess')
    guess = int(input())
    if guess < RanNum:
        print('Your guess is a too low')
    elif guess > RanNum :
        print('Your guess is a too high')
    else :
        break
if guess == RanNum:
    print('Good job, You guessed my number in ' + str(GuessTook) + ' guesses')
else :
    print('Nope i was thinking of ' + str(RanNum))
