import random,sys,time
while True:
    time.sleep(0.7)
    print('to play enter (p) to quit enter (q) ')
    replay = input()
    time.sleep(0.7)
    if replay == "q":
        sys.exit()
    elif replay =="p":
        
        RanNum = random.randint(1,20)
        print('I am thinking of a number between 1 to 20')
        time.sleep(0.7)
        for GuessTook in range(5) :
            time.sleep(0.7)
            print('Take a guess')
            guess = int(input())
            if guess < RanNum - 5:
                print('Your guess is too low')
            elif RanNum - 5 <= guess < RanNum:
                print('Your guess is a little low')
            elif RanNum + 5 >= guess > RanNum:
                print('Your guess is a little high')
            elif guess > RanNum :
                print('Your guess is a too high')
            else :
                break
        if guess == RanNum:
            time.sleep(0.7)
            print('Good job, You guessed my number in ' + str(GuessTook+1) + ' guesses')
        else :
            time.sleep(0.7)
            print('Nope i was thinking of ' + str(RanNum))
    else :
        print('choose apropriate option')
