import random
'''
Game Rules
    Scissors cuts Paper 
    Paper covers Rock 
    Rock crushes Lizard 
    Lizard poisons Spock 
    Spock smashes Scissors 
    Scissors decapitates Lizard
    Lizard eats Paper
    Paper disproves Spock
    Spock vaporizes Rock
    Rock crushes Scissor

Objects are entered by abbreviation: Rock (R), Paper (P), Scissors (S), Lizard (L), Spock (V)
'''


# Wrote out all the rules
def winner(playA, playB):

    match = (playA,playB)

    if match == ('S', 'P') or match == ('P', 'S'):
        return 'S'
    if match == ('P', 'R') or match == ('R', 'P'):
        return 'P'
    if match == ('R', 'L') or match == ('L', 'R'):
        return 'R'
    if match == ('L', 'V') or match == ('V', 'L'):
        return 'L'
    if match == ('V', 'S') or match == ('S', 'V'):
        return 'V'
    if match == ('S', 'L') or match == ('L', 'S'):
        return 'S'
    if match == ('L', 'P') or match == ('P', 'L'):
        return 'L'
    if match == ('P', 'V') or match == ('V', 'P'):
        return 'P'
    if match == ('V', 'R') or match == ('R', 'V'):
        return 'V'
    if match == ('R', 'S') or match == ('S', 'R'):
        return 'R'

    return None


# ask user to input objects
# check if the input is valid
# if the input is valid, return a string that represents the object
# else print out error message and keep asking until getting a vaild input

def player() -> str:
    while True:
        user_input = input("Input the objects: ")
        if user_input == 'R' or user_input == 'P' or user_input == 'S' or user_input == 'L' or user_input == 'V':
            return user_input
        else:
            print("Please enter a correct object")


# randomly picks an object and return the string
def computer() -> str:
    return random.choice(['R', 'P', 'S', 'L', 'V'])


# return True if player wins else False
# if a tie happens, the process is repeated until a winner is found
# print out messages for each round
# print out winner if found and return bool
def game() -> bool:
    names = {'R':'Rock','P': 'Paper', 'S': 'Scissors','L':'Lizard','V':'Spock'}
    while True:
        playa = player()
        assert playa in ['R', 'P', 'S', 'L', 'V']  # assert
        playb = computer()
        assert playb in ['R', 'P', 'S', 'L', 'V']  # assert

        if playa == playb:
            print("Computer also played "+ names[playa])
            continue
        else:
            win = winner(playa, playb)
            if playa == win:
                print("You played "+ names[playa])
                print("Computer played " + names[playb])
                print("You won! "+ names[playa] +" won over "+ names[playb])
                return True
            else:
                print("You played " + names[playa])
                print("Computer played " + names[playb])
                print("Computer won! "+ names[playb] +" won over "+ names[playa])
                return False


# unit test of outputs for functions
assert type(game()) is bool # assert

