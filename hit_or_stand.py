import random
import sys
def hit_or_stand(cards, options, indv):
    while True:
        hit_stand = input('\nWould you like to hit or stand?\nYour total is ' + str(21-indv) + '\n')
        if hit_stand.lower() == 'hit':
            hit = random.choice(options)
            if cards[hit] == 11:
                if indv - 11 < 0:
                    cards[hit] == 1
            else:
                pass
            print(hit + '\n', 'value =', str(cards[hit]))
            hitter = cards[hit]
            if indv < hitter:
                indv = indv - hitter
                print('You busted\nDealer wins')
                return indv
            elif indv == hitter:
                print('Blackjack mffff')
                indv = indv - hitter
                return indv
            else:
                indv = indv - hitter
                del cards[hit]
        elif hit_stand.lower() == 'stand':
            return indv
        else:
            print('please enter valid input')
    