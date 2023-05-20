# Library imports

import time
import random

# Variables
player_health = 50
BOLD = '\033[1m'
ITALIC = '\033[3m'
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
UNDERLINE = "\033[4m"
RESET = '\033[0m'

# functions


def print_with_delay(text):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.01)
    print()


def attack_with_weapon(weapon, damage):
    global ghost_health
    ghost_health -= damage
    time.sleep(0.1)
    print_with_delay("{}, dealing {} points of damage.".format(weapon, damage))
    time.sleep(1)


def heal_player():
    # Restores player's health with a random value between 1 and 30
    global player_health
    health_package = random.randint(1, 30)
    player_health += health_package
    print_with_delay(
        "You find a health package in the treasure chest and gain {} health points.".format(health_package))


# Text image (if needed)

# Intro (Adeola)------------------------------------------------------------------------------------------
print_with_delay(BOLD + LIGHT_RED +
                 "...................Welcome to Enclosed space................" + RESET)
print_with_delay(
    BOLD + YELLOW + "...................Welcome to Enclosed space................" + RESET)
print_with_delay(BOLD + LIGHT_BLUE +
                 "...................Welcome to Enclosed space................" + RESET)
print_with_delay(
    BOLD + GREEN + "...................Welcome to Enclosed space................" + RESET)
print_with_delay(
    BOLD + RED + "...................Welcome to Enclosed space................" + RESET)
print("")
print_with_delay("       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀")
print_with_delay("       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀")
print_with_delay("      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆⠀")
print_with_delay("      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀⠿⣿⡇⠀")
print_with_delay("      ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀")
print_with_delay("      ⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀")
print_with_delay("      ⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀")
print_with_delay("      ⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀")
print_with_delay("      ⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀")
print_with_delay("      ⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀")
print_with_delay("      ⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀")
print_with_delay("      ⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀")
print_with_delay("      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

print("")


player_name = input("what is your name " + GREEN + ":> " + RESET)
print_with_delay(LIGHT_CYAN + BOLD + "{}".format(player_name) +
                 RESET + ",Welcome to Enclosed space!")


# Stats (Adeola)------------------------------------------------------------------------------------------

# wake up instructions

input("Press enter to wake up" + GREEN + ":> " + RESET)
print_with_delay(
    "You wake up in a dimly lit bedroom, disoriented and with no memory of the day before.")
print_with_delay(
    "As you try to collect your thoughts, you hear eerie noises echoing through the house.")
print_with_delay(
    "A sudden realization hits you - you are injured and in need of medical supplies.")
print_with_delay(
    "Determined to uncover the truth, you must find a way out of this haunting nightmare.")


input("Press enter to get up" + GREEN + ":> " + RESET)
print_with_delay(LIGHT_CYAN + BOLD + "{}".format(player_name) +
                 RESET + ",you need to find out about your health.")
input("Press enter to see your health stats" + GREEN + ":> " + RESET)
print_with_delay("Your health is" + GREEN + BOLD +
                 " {} points.".format(player_health))
print_with_delay(RESET + "You find a " + BOLD + RED + "RED KEY" +
                 RESET + " and a " + BOLD + BROWN + "NOTE " + RESET + "on the ground.")

# Inspect the note

input("Press enter to read the note" + GREEN + ":> " + RESET)
print_with_delay(UNDERLINE + ITALIC + YELLOW +
                 "You are in a haunted house, you must find a way to escape" + RESET)
# inspect the key
input("Press enter to inspect the key" + GREEN + ":> " + RESET)
print_with_delay(UNDERLINE + "The " + BOLD + RED + UNDERLINE +
                 "key" + RESET + UNDERLINE + " opens the kitchen door" + RESET)

print_with_delay("You leave the bedroom and enter to the corridor")
print_with_delay("You can see there are 3 doors")

# Corridor0 (Zamir)----------------------------------------------------------------------------------------

corridor_choice = input("Choose " + RED + "RED, " + YELLOW +
                        "YELLOW " + "or " + BLUE + "BLUE door" + GREEN + " :> " + RESET)

while corridor_choice.lower() != "red":
    if corridor_choice.lower() == "yellow" or corridor_choice.lower() == "blue":
        print_with_delay(PURPLE + "This door is locked" + RESET)
        corridor_choice = input(
            "Please choose another door" + GREEN + " :> " + RESET)
    else:
        print_with_delay(BLACK + BOLD + "Choose wisely" + RESET)
        corridor_choice = input("Choose " + RED + "red, " + YELLOW +
                                "yellow " + BLUE + "or blue door" + GREEN + " :> " + RESET)

print_with_delay(LIGHT_GREEN + "You use " + RED + "red key" + LIGHT_GREEN +
                 " to unlock the Kitchen door and enter the room." + RESET)


# Kitchen (Brad) --------------------------------------------------------------------------------------------

ghost_health = 15

print_with_delay("A" + LIGHT_WHITE + ITALIC + " ghost" +
                 RESET + " is waiting for you inside.")

# kitchen battle

print_with_delay(
    "You see a sword and a gun on the table, you use them to attack the ghost")

while ghost_health > 0:
    print_with_delay(GREEN + BOLD + "Your health: {}".format(player_health))
    print_with_delay(LIGHT_WHITE + "Ghost's health: {}".format(ghost_health))
    print_with_delay(RESET + "Choose your action:")
    print_with_delay(UNDERLINE + "1. Attack with a sword")
    print_with_delay(UNDERLINE + "2. Attack with a gun")

    choice = input("Enter your choice (1 or 2)" + GREEN + " :> " + RESET)
    if choice == "1":
        attack_with_weapon(
            LIGHT_RED + "{} strike the ghost with your sword".format(player_name), 5)
    elif choice == "2":
        attack_with_weapon(
            LIGHT_RED + "{} unleash the gun on the ghost".format(player_name), 10)
    else:
        print_with_delay(LIGHT_GRAY + "Invalid choice. Please try again.")

    if ghost_health <= 0:
        print_with_delay(
            LIGHT_GREEN + "Congratulations! You have defeated the ghost.")
        print_with_delay("You see a treasure chest")
        print_with_delay("You find a " + YELLOW + BOLD +
                         "YELLOW KEY " + LIGHT_GREEN + "and a health source" + RESET)
        heal_player()  # Executes the heal_player() function
print_with_delay(
    LIGHT_PURPLE + "You find a health source and your health is increased to {}".format(player_health))
print_with_delay(
    "You have successfully vanquished the ghost and restored your health.")
print_with_delay(
    "You decide to leave the kitchen and continue your exploration.")
print_with_delay(
    "You make your way back to the corridor, ready to face whatever awaits you in your quest." + RESET)

# Corridor1 (Zamir)----------------------------------------------------------------------------------------

corridor_choice = input("Choose " + RED + "RED, " + YELLOW +
                        "YELLOW " + BLUE + "or BLUE door" + GREEN + " :> " + RESET)

while corridor_choice.lower() != "yellow":
    if corridor_choice.lower() == "red":
        print_with_delay(
            DARK_GRAY + "This room is empty, you already have been here" + RESET)
        corridor_choice = input(
            "Please choose another door" + GREEN + " :> " + RESET)
    elif corridor_choice.lower() == "blue":
        print_with_delay(PURPLE + "The door is locked" + RESET)
        corridor_choice = input(
            "Please choose another door" + GREEN + " :> " + RESET)
    else:
        print_with_delay(BLACK + BOLD + "Choose wisely" + RESET)
        corridor_choice = input("Choose " + RED + "RED, " + YELLOW +
                                "YELLOW " + BLUE + "or BLUE door" + GREEN + " :> " + RESET)


# Living room (Maz) --------------------------------------------------------------------------------------------

ghost_health = 25

print_with_delay(LIGHT_GREEN + "You use the " + YELLOW + "yellow key " +
                 LIGHT_GREEN + "to unlock the Living room door and enter the room.")
print_with_delay("Another " + LIGHT_WHITE + ITALIC + "ghost" +
                 LIGHT_GREEN + " awaits you, stronger than before." + RESET)


# Living room battle

print_with_delay(
    "You see a sword and a gun on the table, you use them to attack the ghost")

while ghost_health > 0:
    print_with_delay(GREEN + "Your health: {}".format(player_health))
    print_with_delay(LIGHT_WHITE + "Ghost's health: {}".format(ghost_health))
    print_with_delay(RESET + "Choose your action:")
    print_with_delay("1. Attack with a sword")
    print_with_delay("2. Attack with a gun")

    choice = input("Enter your choice (1 or 2)" + GREEN + " :> " + RESET)
    if choice == "1":
        attack_with_weapon(
            LIGHT_RED + "{} strike the ghost with your sword".format(player_name), 5)
    elif choice == "2":
        attack_with_weapon(
            LIGHT_RED + "{} unleash the gun on the ghost".format(player_name), 10)
    else:
        print_with_delay(LIGHT_GRAY + "Invalid choice. Please try again.")

    if ghost_health <= 0:
        print_with_delay(
            LIGHT_GREEN + "Congratulations! You have defeated the ghost.")
        print_with_delay("You see a treasure chest")
        print_with_delay("You find a " + BLUE + BOLD + "BLUE KEY " +
                         LIGHT_GREEN + "and a health source" + RESET)
        heal_player()  # Executes the heal_player() function
print("You have {} health".format(player_health))
print_with_delay(
    LIGHT_PURPLE + "You have successfully vanquished the ghost and restored your health.")
print_with_delay(
    "You decide to leave the living room and continue your exploration.")
print_with_delay(
    "You make your way back to the corridor, ready to face whatever awaits you in your quest." + RESET)


# Corridor2 (Zamir)----------------------------------------------------------------------------------------

corridor_choice = input("Choose " + RED + "RED, " + YELLOW +
                        "YELLOW " + BLUE + "or BLUE door" + GREEN + " :> " + RESET)

while corridor_choice.lower() != "blue":
    if corridor_choice.lower() == "red" or corridor_choice.lower() == "yellow":
        print_with_delay(
            DARK_GRAY + "This room is empty, you already have been here" + RESET)
        corridor_choice = input(
            "Please choose another door" + GREEN + " :> " + RESET)
    else:
        print_with_delay(BLACK + BOLD + "Choose wisely" + RESET)
        corridor_choice = input("Choose " + RED + "RED, " + YELLOW +
                                "YELLOW " + BLUE + "or BLUE door" + GREEN + " :> " + RESET)

print_with_delay("The bathroom door is open and you can enter")
print_with_delay("You enter the bathroom")


# Bathroom (Faz) --------------------------------------------------------------------------------------------

ghost_health = 45

print_with_delay("You use the " + BLUE + "blue key " + RESET +
                 "to unlock the Bathroom door and enter the room.")
print_with_delay("A stronger" + LIGHT_WHITE + ITALIC + "ghost" +
                 RESET + "lurks inside with a formidable health pool of 50.")

# Bathroom battle

print_with_delay(
    "You see a sword and a gun on the table, you use them to attack the ghost")

while ghost_health > 0:
    print_with_delay(GREEN + "Your health: {}".format(player_health))
    print_with_delay(LIGHT_WHITE + "Ghost's health: {}".format(ghost_health))
    print_with_delay(RESET + "Choose your action:")
    print_with_delay("1. Attack with a sword")
    print_with_delay("2. Attack with a gun")

    choice = input("Enter your choice (1 or 2)" + GREEN + " :> " + RESET)
    if choice == "1":
        attack_with_weapon(
            LIGHT_RED + "{} strike the ghost with your sword".format(player_name), 5)
    elif choice == "2":
        attack_with_weapon(
            LIGHT_RED + "{} unleash the gun on the ghost".format(player_name), 10)
    else:
        print_with_delay(LIGHT_GRAY + "Invalid choice. Please try again.")

    if ghost_health <= 0:
        print_with_delay(LIGHT_GREEN + ITALIC +
                         "Congratulations! You have defeated the ghost.")
        print_with_delay("You find a treasure chest")
        print_with_delay("You open the treasure chest and there is a " +
                         LIGHT_CYAN + BOLD + "FINAL KEY" + RESET)
print_with_delay("You decide to leave the bathroom.")
print_with_delay(
    "You make your way back to the corridor, and a front door appears.")


# Corridor3 (Zamir)----------------------------------------------------------------------------------------

print_with_delay(
    "Congratulations! {}, you possess all keys.".format(player_name))
print_with_delay(
    "The game prompts you to type 'open' to unlock the front door.")
open_door = input("Type 'OPEN'" + GREEN + " :> " + RESET)

if open_door.lower() == "open":
    print_with_delay(GREEN + BOLD + UNDERLINE + "You unlock the front door.")
    print_with_delay(
        "You can now breathe a sigh of relief as the game comes to an end.")
    print_with_delay("Congratulations on your escape!")
else:
    print_with_delay(YELLOW + BOLD + UNDERLINE +
                     "You hesitate to open the door and remain trapped in the haunting house.")
    print_with_delay("Game Over! Your adventure ends here.")