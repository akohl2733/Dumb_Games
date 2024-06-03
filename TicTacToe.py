# tic tac toe
from TicTacCheck import check
# want to initialize each piece as 'O'
dict = {
    'UL': ' ', 'UM': ' ', 'UR': ' ',
    'ML': ' ', 'MM': ' ', 'MR': ' ',
    'BL': ' ', 'BM': ' ', 'BR': ' ',
}

# gives rules to user
print('Vertically - Use U for Upper, M for Middle, and B for Bottom')
print('Horizontally - Use L for Left, M for Middle, and R for Right')
print('(ie. UL, MM, BR)')

# board = dict['UL'] + ' | ' + dict['UM'] + ' | ' + dict['UR'] + '\n' + '_'*9 +'\n'*2 + dict['ML'] + ' | ' + dict['MM'] + ' | ' + dict['MR'] + '\n' + '_'*9 + '\n'*2 + dict['BL'] + ' | ' + dict['BM'] + ' | ' + dict['BR']
# print(board)

x = 0
while True:
    if ' ' not in dict.values():
        print('Draw')
        break
    place = input('Which spot would you like to select?\n')
    if place.upper() not in dict.keys() or dict[place.upper()] != ' ':
        print('Not a valid input retard')
    else:
        if x == 0:
            x+=1
            dict[place.upper()] = 'X'
            if check(dict, 'X') != None:
                print(check(dict, 'X'))
                break
        else:
            x-=1
            dict[place.upper()] = 'O'
            if check(dict, 'O') != None:
                print(check(dict, 'O'))
                break
    board = dict['UL'] + ' | ' + dict['UM'] + ' | ' + dict['UR'] + '\n' + '_'*9 +'\n'*2 + dict['ML'] + ' | ' + dict['MM'] + ' | ' + dict['MR'] + '\n' + '_'*9 + '\n'*2 + dict['BL'] + ' | ' + dict['BM'] + ' | ' + dict['BR']
    print(board)

# want to print out total chart every time
# if someone selects a open space, replace with "X"
# print(dict['UL'] + ' | ' + dict['UM'] + ' | ' + dict['UR'] + '\n' + '_'*9 +'\n'*2 + dict['ML'] + ' | ' + dict['MM'] + ' | ' + dict['MR'] + '\n' + '_'*9 + '\n'*2 + dict['BL'] + ' | ' + dict['BM'] + ' | ' + dict['BR'])
