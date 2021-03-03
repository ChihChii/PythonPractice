from random import randint
import time

money = int(input('How much money do you want hehehe?\n: '))
play = 1

while(money > 0 and play == 1):
    print('Your money is %d now ' % money)

    bet = int(input('How much do you want to bet ? \n Bet : '))
    if(0 < bet <= money):
        print('Banker roll the dice.....')
        time.sleep(2)
        banker1 = randint(1, 6)
        banker2 = randint(1, 6)
        bankersum = banker1+banker2
        print('Banker get %d and %d, total %d' % (banker1, banker2, bankersum))

        print('Player roll the dice.....')
        time.sleep(2)
        player1 = randint(1, 6)
        player2 = randint(1, 6)
        playersum = player1+player2
        print('Player get %d and %d, total %d' % (player1, player2, playersum))

        time.sleep(1)
        if(bankersum > playersum):
            money -= bet
            print('You loss %d ! Your money is %d now !' % (bet, money))
        elif(bankersum < playersum):
            money += bet
            print('You win %d ! Your money is %d now !' % (bet, money))
        else:
            print('Draw !')
            print('Your money is %d now !' % money)

        play = bool(
            input('Do you want to continue ?\n(1 for yes, 0 for no)\n :'))

    else:
        print('Bet fail La!')

if money <= 0:
    print('You dont have enough money, can not play La ! ByeBye !')
else:
    print('Bye ~~~~~~')
