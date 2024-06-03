import random
import sys
import time
from hit_or_stand import hit_or_stand
from deal_func import house_winner

cards = {
    'Ace of Spades': 11, 'Ace of Hearts': 11, 'Ace of Diamonds': 11, 'Ace of Clubs': 11,
    'King of Spades': 10, 'King of Hearts': 10, 'King of Diamonds': 10, 'King of Clubs': 10,
    'Queen of Spades': 10, 'Queen of Hearts': 10, 'Queen of Diamonds': 10, 'Queen of Clubs': 10,
    'Jack of Spades': 10, 'Jack of Hearts': 10, 'Jack of Diamonds': 10, 'Jack of Clubs': 10,
    '10 of Spades': 10, '10 of Hearts': 10, '10 of Diamonds': 10, '10 of Clubs': 10,
    '9 of Spades': 9, '9 of Hearts': 9, '9 of Diamonds': 9, '9 of Clubs': 9,
    '8 of Spades': 8, '8 of Hearts': 8, '8 of Diamonds': 8, '8 of Clubs': 8,
    '7 of Spades': 7, '7 of Hearts': 7, '7 of Diamonds': 7, '7 of Clubs': 7,
    '6 of Spades': 6, '6 of Hearts': 6, '6 of Diamonds': 6, '6 of Clubs': 6,
    '5 of Spades': 5, '5 of Hearts': 5, '5 of Diamonds': 5, '5 of Clubs': 5,
    '4 of Spades': 4, '4 of Hearts': 4, '4 of Diamonds': 4, '4 of Clubs': 4,
    '3 of Spades': 3, '3 of Hearts': 3, '3 of Diamonds': 3, '3 of Clubs': 3,
    '2 of Spades': 2, '2 of Hearts': 2, '2 of Diamonds': 2, '2 of Clubs': 2
}


# set variables needed within this throughout program
indv = 21
dealer = 21
options = list(cards.keys())



# create prorgram for distribution of the first dealer's card
# displays one card that comes out for dealer before you see your cards
# add break to add suspense
print('Dealer card incoming...')
time.sleep(3)
deal_choice = random.choice(options)
print('\nDealer showing ' + deal_choice + '\n' + 'value =', cards[deal_choice])
dealer = dealer - cards[deal_choice]
del cards[deal_choice]
print(21-dealer)
print()



# program for first card of the player
# find random card from remaining cards in dictionary and delete card from remaining deck
print('First card incoming...')
time.sleep(3)
choice = random.choice(options)
print('Your fIrst card: ' + choice + '\n', 'value =', cards[choice])
print()
indv = indv - cards[choice]
del cards[choice]


# program for second you will be given
# this accounts for chance that you get an Ace and want to figure out whether
# you want it to equal 1 or 11
second = random.choice(options)
print('Second card incoming...')
time.sleep(3)
print('Second card: ' + second + '\n', 'value =', cards[second])
if cards[second] == 11:
    pick = input('11 of 1?\n')
    if pick == '11' or pick == '1':
        print(f'You chose {cards[second]}')
        cards[second] == int(pick)
        indv = indv - int(pick)
        del cards[second]
    else:
        print('not valid')
else:
    indv = indv - cards[second]
    del cards[second]



# Checks for chance that you busted (highly unlikely) or got to 21
# in the case that you most likely did not get either, run hit_or_stand 
# and potentially house_winner functinos to determine winner
# if you do bust, make sure the program ends completely to avoid continuation
if indv == 0:
    print('Blackjack!')
elif indv < 0:
    print('Busted son!')
    sys.exit()
else:
    print(str(21 - indv) + '\n')
    if hit_or_stand(cards, options, indv) >= 0:
        print(indv)
        print('You end with ' + str(21-indv) + '\n')
        house_winner(cards, options, indv, dealer)
    else:
        sys.exit()