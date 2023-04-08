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

list = rock, scissors, paper
type = int(
    input(
        "What to do you want to choose for your game? Type 0 for Rock, 1 for scissors or 2 for paper\n"
    ))
if type == 0:
    print(rock)
elif type == 1:
    print(scissors)
else:
    print(paper)

print("computer choice")
random1 = (random.choice(list))
print(random1)

if type == 0 and random1 == scissors:
    print("Hey you win the game!")
elif type == 1 and random1 == rock:
    print("oh no you lose!")
elif type == 1 and random1 == paper:
    print("Hey you win the game!")
elif type == 2 and random1 == scissors:
    print("oh no you lose!")
elif type == 0 and random1 == paper:
    print("oh no you lose!")
elif type == 2 and random1 == rock:
    print("Hey you win the game!")
elif type == 0 and random1 == rock:
    print("GAME DRAW")
elif type == 1 and random1 == scissors:
    print("GAME DRAW")
else:
    print("GAME DRAW")
