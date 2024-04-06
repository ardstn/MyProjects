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
import random
images=[rock,paper,scissors]

user=int(input("what do you choose? 0 for rock, 1 for paper, 2 for scissors.\n"))

if user >= 3 or user < 0:
  print("invalid number")
else:
  print(f"you chose:")
  print(images[user])
  
  computer=random.randint(0,2)
  print(f"computer chose:")
  print(images[computer])
  
  
  if user == 0 and computer == 2:
    print("you win!")
  elif computer == 0 and user == 2:
    print("you lose")
  elif computer > user:
    print("you lose")
  elif computer < user:
    print("you win!")
  elif computer == user:
    print("draw")
  
  
