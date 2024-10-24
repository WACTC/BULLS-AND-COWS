""" project: Bulls and Cows.py
    author: Jaydriel Montes Connolly <jmontes-connolly2709545@woonsocketschools.com>
    author: Rey Montanez <rmontanez2709394@woonsocketschools.com>
    author: Nicholas LaMoore <nlamoore2609056@woonsocketschools.com>

    date written: 10/15/2024

    description: Bulls and Cows!
"""
import random
# Generates a random three digit number and converts it into a string
Input1 = str(random.randint(100, 999))
print("""You must guess the three digit number to win!
You have ten tries to get the correct answer! Good luck!""")
print()

# If any of the integers in any position equal eachother, it rerolls another 3 digit number 
if Input1[0] == Input1[1]:
    Input1 = str(random.randint(100, 999))
if Input1[0] == Input1[2]:
    Input1 = str(random.randint(100, 999))
if Input1[1] == Input1[0]:
    Input1 = str(random.randint(100, 999))
if Input1[1] == Input1[2]:
    Input1 = str(random.randint(100, 999))
if Input1[2] == Input1[0]:
    Input1 = str(random.randint(100, 999))
if Input1[2] == Input1[1]:
    Input1 = str(random.randint(100, 999))

# Variables
nWin = True
Tries = 10
Bulls = 0
Cows = 0

while nWin:
    # Player input
    Guess1 = input("Please guess the three digit number : ")
    print()
    # Ends the game if they guess the number correctly
    if Guess1 == Input1:
        print("""You guessed all three digits of the number correctly!
You Win, congratulations!!!""")
        nWin = False
    else:
        Bulls = 0
        Cows = 0
    
    # Checks if the number in the first, second, or third position is equal to the numbers of the generated numbers in the same positions
    if Guess1[0] == Input1[0]:
        Bulls += 1
    if Guess1[1] == Input1[1]:
        Bulls += 1
    if Guess1[2] == Input1[2]:
        Bulls += 1
    if Guess1[0] == Input1[1]:
        Cows += 1
    if Guess1[0] == Input1[2]:
        Cows += 1
    if Guess1[1] == Input1[0]:
         Cows += 1
    if Guess1[1] == Input1[2]:
        Cows += 1
    if Guess1[2] == Input1[1]:
        Cows += 1
    if Guess1[2] == Input1[0]:
        Cows += 1

    # Prints how many bulls and cows they have. It also prints the amount of tries that the player has left
    print()
    print(f"You have {Bulls} bulls")
    print(f"You have {Cows} cows")
    print(f"You have {Tries} tries left")

    Tries -= 1
    # if the player has no more tries, the game ends
    if Tries < 1:
        print("You have no more tries remaining :(")
        nWin = False

 
