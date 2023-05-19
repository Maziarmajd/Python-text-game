# Library imports

import time
import random

# Variables
player_health = 50


# functions

def attack_with_sword():
    # Reduces the ghost's health by 5 when attacking with a sword
    global ghost_health
    ghost_health -= 5
    time.sleep(0.5)  # Adds a 1-second delay before the next sentence.
    print("You strike the ghost with your sword, dealing 5 points of damage.")
    time.sleep(1)  # Adds a 1-second delay before the next sentence.


def attack_with_gun():
    # Reduces the ghost's health by 10 when attacking with a gun
    global ghost_health
    ghost_health -= 10
    time.sleep(0.5)  # Adds a 0.51-second delay before the next sentence.
    print("You unleash a powerful shot from your gun, dealing 10 points of damage.")
    time.sleep(1)  # Adds a 1-second delay before the next sentence.


def heal_player():
    # Restores player's health with a random value between 1 and 30
    global player_health
    health_package = random.randint(1, 30)
    player_health += health_package
    print("You find a health package in the treasure chest and gain {} health points.".format(
        health_package))


# Text image (if needed)

# Intro (Adeola)------------------------------------------------------------------------------------------
print("...................Welcome to Enclosed space................")
print("...................Welcome to Enclosed space................")
print("...................Welcome to Enclosed space................")
print("...................Welcome to Enclosed space................")
print("      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⣾⣿⣀⡀⠀⢀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⠀⣼⣿⣀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⢀⣴⣾⠀⣠⠀⠀⡀⠘⠛⠋⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣧⣾⡇⣠⡄⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠸⡿⠛⣿⣿⣿⣿⣧⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⣿⡷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⡿⠋⠁⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣶⣶⣶⣶⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⢀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⠋⢁⣀⣀⣀⣤⣴⣶⣿⡇⠀⠀⠀⠀⣀⣴⡇⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⢀⣠⣴⣾⣿⣿⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("      ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("You are in bedroom injured, you need medical supply")
print("Type Health to check you health or type GET UP to leave the bed")


# Stats (Adeola)------------------------------------------------------------------------------------------

# wake up instructions

first_input = (input("> "))
if first_input == "health":
    print("your health is {}".format(player_health))
else:
    print("wrong answer")

second_input = (input("> "))
if second_input == "get up":
    print("leave the bed,look around for clue")

print("You find a key and a note on the ground")

# Inspect the note

input("Press enter to read the note.> ")
print("You are in a haunted house, you must find a way to escape")
# inspect the key
input("Press enter to inspect the key.> ")
print("The key has a red label on it which says Kitchen")

print("You leave the bedroom and enter to the corridor")
print("You can see there are 3 doors")

# Corridor0 (Zamir)----------------------------------------------------------------------------------------

corridor_choice = input("Choose door one, door two, or door three:> ")

while corridor_choice != "door one":
    if corridor_choice == "door two" or corridor_choice == "door three":
        print("This door is locked")
        corridor_choice = input("Please choose another door:> ")
    else:
        print("Choose wisely")
        corridor_choice = input("Choose door one, door two, or door three:> ")

print("The kitchen door is open and you can enter")
print("You enter the kitchen")


# Kitchen (Brad) --------------------------------------------------------------------------------------------

ghost_health = 15

print("You see a very creepy ghost, it threatens you and you must kill it")

# kitchen battle

print("You see a sword and a gun on the table, you use them to attack the ghost")

while ghost_health > 0:
    # Displays player's and ghost's health
    print("Your health: {}".format(player_health))
    print("Ghost's health: {}".format(ghost_health))
    print("Choose your action:")
    print("1. Attack with a sword")
    print("2. Attack with a gun")

    choice = input("Enter your choice (1 or 2):> ")

    if choice == "1":
        attack_with_sword()  # Executes the attack_with_sword() function
    elif choice == "2":
        attack_with_gun()  # Executes the attack_with_gun() function
    else:
        print("Invalid choice. Please try again.")
        continue

    if ghost_health <= 0:
        print("Congratulations! You have defeated the ghost.")
        heal_player()  # Executes the heal_player() function
print("You find a health source and your health is increased to", player_health)
print("You have successfully vanquished the ghost and restored your health.")
print("You decide to leave the kitchen and continue your exploration.")
print("You make your way back to the corridor, ready to face whatever awaits you in your quest.")

#Corridor1 (Zamir)----------------------------------------------------------------------------------------

corridor_choice = input("Choose door one, door two, or door three:> ")

while corridor_choice != "door two":
    if corridor_choice == "door one":
        print("This room is empty, you already have been here")
        corridor_choice = input("Please choose another door:> ")
    elif corridor_choice == "door three":
        print("The door is locked")
        corridor_choice = input("Please choose another door:> ")
    else:
        print("Choose wisely")
        corridor_choice = input("Choose door one, door two, or door three:> ")

print("The living room door is open and you can enter")
print("You enter the living room")


# Living room (Maz) --------------------------------------------------------------------------------------------

ghost_health = 25

print("You see another creepy ghost, it threatens you and you must kill it")


#Living room battle

print("You see a sword and a gun on the table, you use them to attack the ghost")

while ghost_health > 0:
    # Displays player's and ghost's health
    print("Your health: {}".format(player_health))
    print("Ghost's health: {}".format(ghost_health))
    print("Choose your action:")
    print("1. Attack with a sword")
    print("2. Attack with a gun")

    choice = input("Enter your choice (1 or 2):> ")

    if choice == "1":
        attack_with_sword()  # Executes the attack_with_sword() function
    elif choice == "2":
        attack_with_gun()  # Executes the attack_with_gun() function
    else:
        print("Invalid choice. Please try again.")
        continue

    if ghost_health <= 0:
        print("Congratulations! You have defeated the ghost.")
        heal_player()  # Executes the heal_player() function
print("You have {} health".format(player_health))
print("You have successfully vanquished the ghost and restored your health.")
print("You decide to leave the living room and continue your exploration.")
print("You make your way back to the corridor, ready to face whatever awaits you in your quest.")



#Corridor2 (Zamir)----------------------------------------------------------------------------------------

corridor_choice = input("Choose door one, door two, or door three:> ")

while corridor_choice != "door three":
    if corridor_choice == "door one" or corridor_choice == "door two":
        print("This room is empty, you already have been here")
        corridor_choice = input("Please choose another door: ")
    else:
        print("Choose wisely")
        corridor_choice = input("Choose door one, door two, or door three: ")

print("The bathroom door is open and you can enter")
print("You enter the bathroom")


# Bathroom (Faz) --------------------------------------------------------------------------------------------

ghost_health = 45

print("You see another creepy ghost, it threatens you and you must kill it")

#Bathroom battle

print("You see a sword and a gun on the table, you use them to attack the ghost")

while ghost_health > 0:
    # Displays player's and ghost's health
    print("Your health: {}".format(player_health))
    print("Ghost's health: {}".format(ghost_health))
    print("Choose your action:")
    print("1. Attack with a sword")
    print("2. Attack with a gun")

    choice = input("Enter your choice (1 or 2):> ")

    if choice == "1":
        attack_with_sword()  # Executes the attack_with_sword() function
    elif choice == "2":
        attack_with_gun()  # Executes the attack_with_gun() function
    else:
        print("Invalid choice. Please try again.")
        continue

    if ghost_health <= 0:
        print("Congratulations! You have defeated the ghost.")
        heal_player()  # Executes the heal_player() function
print("You have {} health".format(player_health))
print("You have successfully vanquished the ghost and restored your health.")
print("You decide to leave the bathroom and continue your exploration.")
print("You make your way back to the corridor, ready to face whatever awaits you in your quest.")


#Corridor3 (Zamir)----------------------------------------------------------------------------------------

print("Congratulations! You possess all three keys.")
print("The game prompts you to type 'open' to unlock the front door.")
open_door = input("Type 'open':> ")

if open_door.lower() == "open":
    print("You unlock the front door.")
    print("You can now breathe a sigh of relief as the game comes to an end.")
    print("Congratulations on your escape!")
else:
    print("You hesitate to open the door and remain trapped in the haunting house.")
    print("Game Over! Your adventure ends here.")