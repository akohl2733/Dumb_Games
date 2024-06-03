import random
import time
def house_winner(cards, options, indv, dealer):

    while True:

        if dealer >= indv and dealer > 4:
            print('Dealer Total: ' + str(21 - dealer) + '\nAnother card incoming...')
            time.sleep(3)
            kill = random.choice(options)
            killer = cards[kill]
            print(f'Dealer drew {kill}\n' + 'value: ' + str(killer))
            dealer = dealer - killer
            # print(dealer)
            print()

            if killer > (dealer + killer):
                print('Dealer Bust. You win!')
                break

            elif dealer <= 4 and dealer < indv:
                print('dealer wins')
                break

            elif dealer <= 4 and dealer == indv:
                print('Draw. Push to next game.')
                break

            elif dealer <= 4 and dealer > indv:
                print('You win!')
                break

            else:
                del cards[kill]
                
        else:
            break

    
