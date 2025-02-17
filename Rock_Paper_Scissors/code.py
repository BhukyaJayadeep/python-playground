import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Rock_Paper_Scissors = [rock, paper, scissors]
Computer_choice = random.choice(Rock_Paper_Scissors)
try:
    Player_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))
    if Player_choice < 0 or Player_choice > 2:
        print("You entered an invalid number, You Lose!")
    else:
        print('Computer Choice:')
        print(Computer_choice)
        print('Player Choice:')
        print(Rock_Paper_Scissors[Player_choice])
        if Computer_choice == Rock_Paper_Scissors[Player_choice]:
            print('Draw')
        elif (Computer_choice == rock and Rock_Paper_Scissors[Player_choice] == paper) or \
             (Computer_choice == paper and Rock_Paper_Scissors[Player_choice] == scissors) or \
             (Computer_choice == scissors and Rock_Paper_Scissors[Player_choice] == rock):
            print("You Win!")
        else:
            print('You Lose!')
except:
    print("You entered an invalid value or Symbol, You Lose!")
