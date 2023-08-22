# import random module
import random
# print multi line instructions
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper >>>> Paper wins \n"
      + "Rock vs Scissors >>>> Rock wins \n"
      + "Paper vs Scissors >>>> Scissor wins \n")

while True:
    print('Enter your choice \n 1- Rock \n 2- Paper \n 3- Scissor')
    # user input
    choice = int(input('Enter your Choice : '))
    # Or is a short circuit operator
    # if any one of the condition is true then it return true
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice : "))
    # initialize value of choice_name variable corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissor'
    # print user choice
    print('User choice is \n ', choice_name)
    print('Now Computer Turn...')
    # Now computer chooses any number randomly,among 1,2,3 using randint
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'PapeR'
    else:
        comp_choice_name = 'ScissoR'
    print('Computer Choice is \n', comp_choice_name)
    print(choice_name+' Vs ' + comp_choice_name)
    # we need to check of a draw
    if choice == comp_choice:
        print('Its a Draw', end='')
        result = 'DRAW'
    # condition for winning
    if (choice == 1 and comp_choice == 2):
        print('PAPER WINS', end='')
        result = 'PapeR'
    elif (choice == 2 and comp_choice == 1):
        print('PAPER WINS ', end='')
        result = 'Paper'

    if (choice == 1 and comp_choice == 3):
        print('ROCK WINS \n', end='')
        result = 'Rock'
    elif (choice == 3 and comp_choice == 1):
        print('ROCK WINS \n', end='')
        result = 'RocK'

    if (choice == 2 and comp_choice == 3):
        print('SCISSOR WINS', end='')
        result = 'ScissoR'
    elif (choice == 3 and comp_choice == 2):
        print('SCISSOR WINS', end='')
        result = 'Rock'
    # printing either user or computer wins or draw
    if result == 'DRAW':
        print('<<--IT\'S A TIE-->>')
    if result == choice_name:
        print('<<--USER WINS-->>')
    else:
        print('<<--COMPUTER WINS-->>')
    print('Do you want to play again? (y/n)')
    ans = input().lower()
    if ans == 'n':
        break
print('Thanks for playing.!')
