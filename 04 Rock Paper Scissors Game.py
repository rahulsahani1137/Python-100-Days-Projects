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
RPS = [rock,paper,scissors]
userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(RPS[userInput])

computerChoice = random.randint(0,2)
print("Computer's Hand: ")
print(RPS[computerChoice])

if userInput > 2 or userInput < 0:
    print("Invalid User Input")
elif computerChoice == userInput:
    print("It's a DRAW!")
elif (userInput == 0 and computerChoice == 2) or (userInput == 1 and computerChoice == 0) or (userInput == 2 and computerChoice == 1):
    print("You WIN!")
else:
    print("You LOOSE!")
