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

#Write your code below this line 👇
game_images = [rock, paper, scissors]
user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))
if user_pick >=3 or user_pick <0:
    print("You typed the wrong number, you lose")
else:
    print(game_images[user_pick])
    
comp_pick = random.randint(0, 2)
print("Computer threw:")
print(game_images[comp_pick])


if user_pick == 0 and comp_pick == 2:
    print("You win!")
elif comp_pick == 0 and user_pick == 2:
    print("Oh no, you lost!")
elif comp_pick > user_pick:
    print("Oh no, you lost")
elif user_pick > comp_pick:
    print("You win!")
elif comp_pick == user_pick:
    print("Its a draw")
