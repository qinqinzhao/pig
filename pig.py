import random


def main():
    '''This is where the program will start execution.'''
    computer_score = 0
    human_score = 0
    instructions()
    while True:
        computer_score += computer_move(computer_score, human_score)
        human_score += human_move(computer_score, human_score)
        if is_game_over(computer_score, human_score):
            show_results(computer_score, human_score)
            break
            

def instructions():
    '''Tells the user the rules of the game.'''
    print ('"Pig" is a very simple game. Two players take turns; on each turn, a player \n'
          'rolls a six-sided dice as many times as she wishes, or until she rolls a 1. \n'
          'Each number she rolls, except a 1, is added to her score this turn; but if \n'
          'she rolls a 1, her score for this turn is zero, and her turn ends. At the end \n'
          'of each turn, the score for that turn is added to the player\'s total score. \n'
          'The first player to reach or exceed 100 wins. \n'
          '  \n'
          'For example: \n' 
          '* Alice rolls 3, 5, 3, 6, and stops. Her score is now 19. \n'
          '* Bob rolls 5, 4, 6, 6, 2, and stops. His score is now 23. \n'
          '* Alice rolls 5, 3, 3, 5, 4, and stops. Her score is now 39 (19 + 20). \n' 
          '* Bob rolls 4, 6, 1. He has to stop, and his score is still 23 (23 + 0). \n'
          '* Etc. \n'
          '  \n'
          'As defined above, the first player has an advantage. To make the game more \n'
          'fair, we will say that if the first player reaches or exceeds 100, the second \n'
          'player gets one additional turn. (If the second player is the first to reach \n'
          '100, the first player does not get an additional turn.)\n'
          '  \n'
          'You will play against the computer. The computer always goes first, so you \n'
          'get one more turn if the computer is the first to reach 100. \n'
          '  \n'
          'If both players are tied with 100 or more, each gets another turn until the \n'
          'tie is broken. \n'
          '  \n'
          'Let\'s start! \n'
          '  \n'
          '****** \n'
          '  ')


def roll():
    '''Returns a random number in the range 1 to 6, inclusive.'''
    roll_number = random.randint(1, 6)
    return roll_number


def ask_yes_or_no(prompt):
    '''Prints the prompt as a question to the user, for example, "Roll again? ". '''
    '''If the user responds with a string whose first character is 'y' or 'Y', the function returns True. '''
    '''If the user responds with a string whose first character is 'n' or 'N', the function returns False. '''
    '''Any other response will cause the question to be repeated until the user provides an acceptable response.'''
    answer = input(prompt)
    if answer != "" and (answer[0] == "Y" or answer[0] == "y"):
        return True
    elif answer != "" and (answer[0] == "N" or answer[0] == "n"):
        return False
    else:
        return ask_yes_or_no(prompt)


def human_move(computer_score, human_score):
    '''Tells the user both her current score and the computer's score, and how far behind (or ahead) she is. '''
    '''Then repeatedly asks whether the user wants to roll again. This continues until either:'''
    ''' * The user decides not to roll again. The function should return the total of the rolls made during this move.'''
    ''' * The user rolls a 1. The function should return 0.'''
    human_move_score = 0 # human_move_score is the total score the player gets in this turn.
    human_roll = roll() 
    print ("You rolled " + str(human_roll) + ".")
    if human_roll == 1:
        print ("Your current score is " + str(human_score - human_move_score) + ".")
        return 0
    else:
        while human_roll != 1: 
            human_move_score += human_roll
            human_score += human_roll
            print ("Your current score is " + str(human_score) + ".\n"
                  "The computer's score is " + str(computer_score) + ".")
            if human_score >= computer_score:
                ahead = human_score - computer_score
                print ("You are " + str(ahead) + " ahead of the computer.")
            else:
                behind = computer_score - human_score
                print ("You are " + str(behind) + " behind the computer.")
            roll_again = ask_yes_or_no('Do you want to roll again? Please type "Y" or "N".')
            if roll_again:
                human_roll = roll()
                print ("You rolled " + str(human_roll) + ".")
            else:
                return human_move_score
        print ("Your current score is " + str(human_score - human_move_score) + ".")
        return 0
    

def computer_move(computer_score, human_score):
    '''The computer rolls some number of times, displays the result of each roll, '''
    '''and the function returns the result (either 0 or the total of the rolls). '''
    computer_move_score = 0 # computer_move_score is the total score the computer gets in this turn.
    computer_roll = roll()
    print ("The computer rolled " + str(computer_roll) + ".")
    if computer_roll == 1:
        print ("The computer's current score is " + str(computer_score - computer_move_score) + ".")
        return 0
    else:
        while computer_roll != 1:
            computer_move_score += computer_roll
            computer_score += computer_roll
            print ("The computer's current score is " + str(computer_score) + ".")
            if computer_move_score <= 6 or computer_score - human_score <= 0:
                computer_roll = roll()
                print ("The computer rolled " + str(computer_roll) + ".")
            else:
                return computer_move_score
        print ("The computer's current score is " + str(computer_score - computer_move_score) + ".")
        return 0


def is_game_over(computer_score, human_score):
    '''Determines whether the game is over.'''
    '''Returns True if either player has 100 or more, and the players are not tied, otherwise it returns False.'''
    if (computer_score >= 100 or human_score >= 100) and computer_score != human_score:
        return True
    else:
        return False


def show_results(computer_score, human_score):
    '''Tells whether the human won or lost, and by how much.'''
    if human_score > computer_score:
        print ("You won the computer by " + str(human_score - computer_score) + ".")
    else:
        print ("You lost out to the computer by " + str(computer_score - human_score) + ".")
        

main()
