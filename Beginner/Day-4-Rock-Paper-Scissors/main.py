import random

hand_gestures = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''','''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

choice_name = ["Rock", "Paper", "Scissors"]

gamer_choice =  int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
print(f"{hand_gestures[gamer_choice]} You chose {choice_name[gamer_choice]}")
print(f"{hand_gestures[computer_choice]}Computer chose {choice_name[computer_choice]}")

# if the player chooses rock
if gamer_choice == 0 and computer_choice == 0:
    print("Draw.")
elif gamer_choice == 0 and computer_choice == 1:
    print("Computer wins!")
elif gamer_choice == 0 and computer_choice == 2:
    print("You win!")

#if the player chooses paper
elif gamer_choice == 1 and computer_choice == 0:
    print("You win!")
elif gamer_choice == 1 and computer_choice == 1:
    print("Draw.")
elif gamer_choice == 1 and computer_choice == 2:
    print("Computer wins!")

# if the player chooses scissors
elif gamer_choice == 2 and computer_choice == 0:
    print("Computer wins!")
elif gamer_choice == 2 and computer_choice == 1:
    print("You win!")
elif gamer_choice == 2 and computer_choice == 2:
    print("Draw.")