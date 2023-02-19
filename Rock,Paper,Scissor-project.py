# importing the random
import random

# Step 1: Tack input from the user
# user_choice = "ROCK" "PAPER" "SCISSOR"
# user_choice.lower()
user_choice = input('Choice Your Weapon[Rock,Paper,Scissor]: ').lower() 

# random choice ['Rock', 'Paper', 'Scissor']
# this cammand will pick a string randomly from 'Rock', 'Paper', 'Scissor'
# and assigin it to the coputer _choice variable
computer_choice = random.choice(['rock', 'paper', 'scissor'])

# print the input taken 
print('User_choice: ', user_choice)
print('Computer_choice: ', computer_choice)

# lets Create the logics
if user_choice == 'rock' and computer_choice == 'rock':
 print('Game Is Draw')
elif user_choice == 'rock' and computer_choice == 'paper':
 print('Computer Won')
elif user_choice == 'rock' and computer_choice == 'scissor':
 print('User Won')
elif user_choice == 'paper' and computer_choice == 'rock':
 print('User Won')
elif user_choice == 'paper' and computer_choice == 'paper':
 print('Game Is Draw')
elif user_choice == 'paper' and computer_choice == 'scissor':
 print('Computer Won')
elif user_choice == 'scissor' and computer_choice == 'rock':
  print('Computer Won')
elif user_choice == 'scissor' and computer_choice == 'paper':
  print('User Won')
elif user_choice == 'scissor' and computer_choice == 'scissor':
  print('Game Is Draw')
else:
  print('Invalid case')
