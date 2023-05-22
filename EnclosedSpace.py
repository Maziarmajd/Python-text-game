# Library imports

import time
import random
from playsound import playsound

# Sound imports


# Global Variables
player_health = 100

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

# Global functions

#


def print_with_delay(text):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(0.01)
    print()


def attack_with_weapon(weapon, damage):
    global ghost_health
    global player_health
    ghost_health -= damage
    if ghost_health > 0:
        ghost_attack = random.randint(1, 20)
        player_health -= ghost_attack
        playsound("Sounds/ghostattacks.mp3")
    else:
        ghost_attack = 0
    time.sleep(0.1)
    print_with_delay("{}, dealing {} points of damage.".format(weapon, damage))
    time.sleep(0.7)


# healing package


def heal_player():
    # Restores player's health with a random value between 1 and 30
    global player_health
    health_package = random.randint(1, 30)
    player_health += health_package
    playsound("Sounds/health.mp3")
    print_with_delay(
        "You search an old looking treasure chest that has strange markings on it. Inside it there are medical supplies. You use them and gain {} health points".format(health_package))


playsound("Sounds/intro.mp3", block=False)

# Intro (Adeola)------------------------------------------------------------------------------------------

print_with_delay(
    "--------------------------------------- TEAM ONE PRESENTS: -----------------------------------------------------------------")
print_with_delay(
    "----------------------------------------------------------------------------------------------------------------------------")
print("")
print(RED + "▓█████  ███▄    █  ▄████▄   ██▓     ▒█████    ██████ ▓█████ ▓█████▄      ██████  ██▓███   ▄▄▄       ▄████▄  ▓█████")
print(RED + "▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀ ▒██▀ ██▌   ▒██    ▒ ▓██░  ██▒▒████▄    ▒██▀ ▀█  ▓█   ▀")
print(RED + "▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▒██░    ▒██░  ██▒░ ▓██▄   ▒███   ░██   █▌   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ ▒███")
print(RED + "▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄ ░▓█▄   ▌     ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄")
print(RED + "░▒████▒▒██░   ▓██░▒ ▓███▀ ░░██████▒░ ████▓▒░▒██████▒▒░▒████▒░▒████▓    ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░░▒████▒")
print(RED + "░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▒▓  ▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░")
print(RED + " ░ ░  ░░ ░░   ░ ▒░  ░  ▒   ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░ ▒  ▒    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░  ░  ▒    ░ ░  ░")
print(RED + "   ░      ░   ░ ░ ░          ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░    ░ ░  ░    ░  ░  ░  ░░         ░   ▒   ░           ░   ")
print(RED + "   ░  ░         ░ ░ ░          ░  ░    ░ ░        ░     ░  ░   ░             ░                 ░  ░░ ░         ░  ░")


print("" + RESET)
print_with_delay("       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀                  ")
print_with_delay("       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀                  ")
print_with_delay("      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆                    ")
print_with_delay("      ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀                   ")
print_with_delay("      ⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀                  ")
print_with_delay("      ⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀                 ")
print_with_delay("      ⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀                  ")
print_with_delay("      ⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀                 ")
print_with_delay("      ⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀                  ")
print_with_delay("      ⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀                ")
print_with_delay("      ⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀               ")
print_with_delay("      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀              ")

print("")
playsound("Sounds/ghostIntro.mp3")

player_name = input("what is your name " + GREEN + ":> " + RESET)
print_with_delay(LIGHT_CYAN + BOLD + "{}".format(player_name) +
                 RESET + ",Welcome to Enclosed space!")


# Stats (Adeola)------------------------------------------------------------------------------------------

# wake up instructions

input("Press enter to wake up" + GREEN + ":> " + RESET)


print_with_delay(
    "You wake up in a daze, in a dimly lit bedroom, you can’t remember a thing about the day before but have an overwhelming sense of dread ")
print_with_delay(
    "As you try to collect your thoughts, you hear eerie noises echoing through the house.")
playsound("Sounds/distantghosts.mp3", block=False)
print_with_delay(
    "You look down and see blood on the side of your torso and that your leg is bruised in an odd pattern that looks almost like a skull? Who or what could have done this? What do they want with you? ")
print_with_delay(
    "Determined to uncover the truth, you must find a way out of this haunting nightmare.")

playsound("Sounds/suspense.mp3", block=False)
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
playsound("Sounds/note.mp3", block=False)
print_with_delay(UNDERLINE + ITALIC + YELLOW +
                 "Whoever reads this note. This house was once my family home, but has been overtaken by spiritual forces beyond our understanding or control. They are ghosts. I was hesitant to accept that myself. You must find a way to escape this place before you too are victim to them- There are keys to every room but only one opens the front door. I am leaving this note in case anyone finds it. I know not whether I will make it out. – Dated 1700… " + RESET)
# inspect the key
input("Press enter to inspect the key" + GREEN + ":> " + RESET)
playsound("Sounds/key.mp3", block=False)
print_with_delay(UNDERLINE + "The " + BOLD + RED + UNDERLINE +
                 "key" + RESET + UNDERLINE + " opens the kitchen door" + RESET)
print_with_delay("")
playsound("Sounds/door1.mp3", block=False)
print_with_delay(
    "You decide you have to leave the bedroom and go into the corridor ")
print_with_delay("Your vision is slightly fuzzy but you can see 3 doors  ")

# Corridor0 (Zamir)----------------------------------------------------------------------------------------

corridor_choice = input("Choose " + RED + "RED, " + YELLOW +
                        "YELLOW " + "or " + BLUE + "BLUE door" + GREEN + " :> " + RESET)

while corridor_choice.lower() != "red":
    if corridor_choice.lower() == "yellow" or corridor_choice.lower() == "blue":
        playsound("Sounds/lock door.mp3")
        print_with_delay(PURPLE + "This door is locked" + RESET)
        corridor_choice = input(
            "Please choose another door" + GREEN + " :> " + RESET)
    else:
        print_with_delay(BLACK + BOLD + "Choose wisely" + RESET)
        corridor_choice = input("Choose " + RED + "red, " + YELLOW +
                                "yellow " + BLUE + "or blue door" + GREEN + " :> " + RESET)
playsound("Sounds/unlockthedoor.mp3")
print_with_delay(LIGHT_GREEN + "You use " + RED + "red key" + LIGHT_GREEN +
                 " to unlock the Kitchen door and enter the room." + RESET)
playsound("Sounds/door.mp3")
# Kitchen (Brad) --------------------------------------------------------------------------------------------

ghost_health = 15


print_with_delay("A" + LIGHT_WHITE + ITALIC + " ghost" +
                 RESET + " is waiting for you inside.")
playsound("Sounds/ghost1.mp3", block=False)
print(RED + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀")
print(RED + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀")
print(RED + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀")
print(RED + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆⠀")
print(RED + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀⠿⣿⡇⠀")
print(RED + "⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀")
print(RED + "⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀")
print(RED + "⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀")
print(RED + "⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀")
print(RED + "⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀")
print(RED + "⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀")
print(RED + "⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀")
print(RED + "⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀")
print(RED + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(RED + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + RESET)


# kitchen battle

print_with_delay(
    "You have the sword and the gun to hand. Use them to attack the ghost ")

while ghost_health > 0:
    print_with_delay(GREEN + BOLD + "Your health: {}".format(player_health))
    print_with_delay(LIGHT_WHITE + "Ghost's health: {}".format(ghost_health))
    print_with_delay(RESET + "Choose your action:")
    print_with_delay(UNDERLINE + "1. Attack with a sword")
    print_with_delay(UNDERLINE + "2. Attack with a gun")
    time.sleep(0.5)
    choice = input("Enter your choice (1 or 2)" + GREEN + " :> " + RESET)
    if choice == "1":
        attack_with_weapon(
            LIGHT_RED + "{} strike the ghost with your sword".format(player_name), 5)
        playsound("Sounds/sword.mp3")
    elif choice == "2":
        attack_with_weapon(
            LIGHT_RED + "{} unleash the gun on the ghost".format(player_name), 10)
        playsound("Sounds/gun.mp3")
    else:
        print_with_delay(LIGHT_GRAY + "Invalid choice. Please try again.")

    if player_health <= 0:
        print_with_delay(
            "The ghost overwhelms you, and you succumb to its haunting presence.")
        print_with_delay(
            "Game Over! You have to restart your adventure from the beginning.")
        playsound("Sounds/ghostlaugh1.mp3", block=False)
        print("")
        print_with_delay(
            RED + "██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗")
        print_with_delay(
            RED + "██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
        print_with_delay(
            RED + "██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
        print_with_delay(
            RED + "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
        print_with_delay(
            RED + "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
        print_with_delay(
            RED + "╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
        print_with_delay(YELLOW + "CREATED BY: TEAM ONE")
        print_with_delay(
            YELLOW + "ADEOLA, BRADLEY, FAZAL, PAYIKENE, MAZIAR, ZAMIR")
        print_with_delay(YELLOW + "THANK YOU" + RESET)

        exit()

    if ghost_health <= 0:
        print_with_delay(
            LIGHT_GREEN + "Congratulations! You have defeated the ghost.")
        print_with_delay("You see a treasure chest")
        print_with_delay("You find a " + YELLOW + BOLD +
                         "YELLOW KEY " + LIGHT_GREEN + "and a health source" + RESET)
        heal_player()  # Executes the heal_player() function
        print_with_delay(
            LIGHT_PURPLE + "Your health is increased to {}".format(player_health))
        print_with_delay(
            "You have successfully vanquished the ghost and restored your health.")
        print_with_delay(
            "You have a bad feeling that the ghosts will only get harder to kill as the night goes on ")
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
        playsound("Sounds/lock door.mp3")
        print_with_delay(PURPLE + "The door is locked" + RESET)
        corridor_choice = input(
            "Please choose another door" + GREEN + " :> " + RESET)
    else:
        print_with_delay(BLACK + BOLD + "Choose wisely" + RESET)
        corridor_choice = input("Choose " + RED + "RED, " + YELLOW +
                                "YELLOW " + BLUE + "or BLUE door" + GREEN + " :> " + RESET)


# Living room (Maz) --------------------------------------------------------------------------------------------

ghost_health = 25
playsound("Sounds/unlockthedoor.mp3")
print_with_delay(LIGHT_GREEN + "You use the " + YELLOW + "yellow key " +
                 LIGHT_GREEN + "to unlock the Living room door and enter the room.")
playsound("Sounds/door.mp3")

print_with_delay("Another " + LIGHT_WHITE + ITALIC + "ghost" +
                 LIGHT_GREEN + " awaits you, stronger than be" + RESET)
playsound("Sounds/ghost2.mp3", block=False)

print(YELLOW + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀")
print(YELLOW + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀")
print(YELLOW + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀")
print(YELLOW + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆⠀")
print(YELLOW + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀⠿⣿⡇⠀")
print(YELLOW + "⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀")
print(YELLOW + "⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀")
print(YELLOW + "⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀")
print(YELLOW + "⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀")
print(YELLOW + "⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀")
print(YELLOW + "⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀")
print(YELLOW + "⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀")
print(YELLOW + "⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀")
print(YELLOW + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(YELLOW + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + RESET)


# Living room battle

print_with_delay(
    "You see a sword and a gun on the table, you use them to attack the ghost")

while ghost_health > 0:
    print_with_delay(GREEN + "Your health: {}".format(player_health))
    print_with_delay(LIGHT_WHITE + "Ghost's health: {}".format(ghost_health))
    print_with_delay(RESET + "Choose your action:")
    print_with_delay("1. Attack with a sword")
    print_with_delay("2. Attack with a gun")
    time.sleep(0.5)
    choice = input("Enter your choice (1 or 2)" + GREEN + " :> " + RESET)
    if choice == "1":
        attack_with_weapon(
            LIGHT_RED + "{} strike the ghost with your sword".format(player_name), 5)
        playsound("Sounds/sword.mp3")
    elif choice == "2":
        attack_with_weapon(
            LIGHT_RED + "{} unleash the gun on the ghost".format(player_name), 10)
        playsound("Sounds/gun.mp3")
    else:
        print_with_delay(LIGHT_GRAY + "Invalid choice. Please try again.")
    if player_health <= 0:
        print_with_delay(
            "The ghost overwhelms you, and you succumb to its haunting presence.")
        print_with_delay(
            "Game Over! You have to restart your adventure from the beginning.")
        playsound("Sounds/ghostlaugh2.mp3")
        print("")
        print_with_delay(
            RED + "██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗")
        print_with_delay(
            RED + "██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
        print_with_delay(
            RED + "██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
        print_with_delay(
            RED + "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
        print_with_delay(
            RED + "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
        print_with_delay(
            RED + "╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
        print_with_delay(YELLOW + "CREATED BY: TEAM ONE")
        print_with_delay(
            YELLOW + "ADEOLA, BRADLEY, FAZAL, PAYIKENE, MAZIAR, ZAMIR")
        print_with_delay(YELLOW + "THANK YOU" + RESET)

        exit()

    if ghost_health <= 0:
        print_with_delay(
            LIGHT_GREEN + "Congratulations! You have defeated the ghost.")
        print_with_delay("You see a treasure chest")
        print_with_delay("You find a " + BLUE + BOLD + "BLUE KEY " +
                         LIGHT_GREEN + "and a health source" + RESET)
        heal_player()  # Executes the heal_player() function
print("You have {} health".format(player_health))
print_with_delay(
    LIGHT_PURPLE + "The ghost is defeated. Your health is restored. You think it might be adrenaline but you don’t care ")
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


# Bathroom (Faz) --------------------------------------------------------------------------------------------

ghost_health = 45
playsound("Sounds/unlockthedoor.mp3")
print_with_delay("You use the " + BLUE + "blue key " + RESET +
                 "to unlock the Bathroom door and enter the room.")
playsound("Sounds/door.mp3")
print_with_delay("A stronger" + LIGHT_WHITE + ITALIC + "ghost" +
                 RESET + "lurks insid. You are frightened and frustrated that this ghost is stronger still having barely escaped last time. You decide to fight it anyway  ")
playsound("Sounds/ghost3.mp3", block=False)

print(BLUE + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀")
print(BLUE + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀")
print(BLUE + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣆⠀⠀")
print(BLUE + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⠁⠀⠿⢿⣿⡿⣿⣿⡆⠀")
print(BLUE + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣴⣿⠃⠀⠿⣿⡇⠀")
print(BLUE + "⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠋⠁⣿⠟⣿⣿⢿⣧⣤⣴⣿⡇⠀")
print(BLUE + "⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠘⠁⢸⠟⢻⣿⡿⠀⠀")
print(BLUE + "⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣇⢀⣤⠀⠀⠀⠀⠘⣿⠃⠀⠀")
print(BLUE + "⠀⠀⠀⠀⠀⢈⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣿⢀⣴⣾⠇⠀⠀⠀")
print(BLUE + "⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀")
print(BLUE + "⠀⠀⠉⠉⠉⠉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀")
print(BLUE + "⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀")
print(BLUE + "⠀⠀⣴⡾⠿⠿⠿⠛⠋⠉⠀⢸⣿⣿⣿⣿⠿⠋⢸⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀")
print(BLUE + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠟⠋⠁⠀⠀⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print(BLUE + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀" + RESET)

# Bathroom battle

print_with_delay(
    "There is another sword and gun at your feet. You are relieved. You launch yourself at the ghost and fight it. ")

while ghost_health > 0:
    print_with_delay(GREEN + "Your health: {}".format(player_health))
    print_with_delay(LIGHT_WHITE + "Ghost's health: {}".format(ghost_health))
    print_with_delay(RESET + "Choose your action:")
    print_with_delay("1. Attack with a sword")
    print_with_delay("2. Attack with a gun")
    time.sleep(0.5)
    choice = input("Enter your choice (1 or 2)" + GREEN + " :> " + RESET)
    if choice == "1":
        attack_with_weapon(
            LIGHT_RED + "{} strike the ghost with your sword".format(player_name), 5)
        playsound("Sounds/sword.mp3")
    elif choice == "2":
        attack_with_weapon(
            LIGHT_RED + "{} unleash the gun on the ghost".format(player_name), 10)
        playsound("Sounds/gun.mp3")
    else:
        print_with_delay(LIGHT_GRAY + "Invalid choice. Please try again.")

    if player_health <= 0:
        print_with_delay(
            "The ghost overwhelms you, and you succumb to its haunting presence.")
        print_with_delay(
            "Game Over! You have to restart your adventure from the beginning.")
        playsound("Sounds/ghostlaugh3.mp3", block=False)
        print("")
        print_with_delay(
            RED + "██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗")
        print_with_delay(
            RED + "██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
        print_with_delay(
            RED + "██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
        print_with_delay(
            RED + "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
        print_with_delay(
            RED + "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
        print_with_delay(
            RED + "╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
        print_with_delay(YELLOW + "CREATED BY: TEAM ONE")
        print_with_delay(
            YELLOW + "ADEOLA, BRADLEY, FAZAL, PAYIKENE, MAZIAR, ZAMIR")
        print_with_delay(YELLOW + "THANK YOU" + RESET)

        exit()

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
    playsound("Sounds/unlockthedoor.mp3")
    print_with_delay(GREEN + BOLD + UNDERLINE + "You unlock the front door.")
    playsound("Sounds/Finaldoor.mp3")
    print_with_delay(
        "You can now breathe a sigh of relief as the game comes to an end.")
    print_with_delay("Congratulations on your escape!")
    playsound("Sounds/the end.mp3", block=False)
    print("")
    print_with_delay(
        "░█████╗░░█████╗░███╗░░██╗░██████╗░██████╗░░█████╗░████████╗██╗░░░██╗██╗░░░░░░█████╗░████████╗██╗░█████╗░███╗░░██╗██╗░██████╗██╗")
    print_with_delay(
        "██╔══██╗██╔══██╗████╗░██║██╔════╝░██╔══██╗██╔══██╗╚══██╔══╝██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║╚█║██╔════╝██║")
    print_with_delay(
        "██║░░╚═╝██║░░██║██╔██╗██║██║░░██╗░██████╔╝███████║░░░██║░░░██║░░░██║██║░░░░░███████║░░░██║░░░██║██║░░██║██╔██╗██║░╚╝╚█████╗░██║")
    print_with_delay(
        "██║░░██╗██║░░██║██║╚████║██║░░╚██╗██╔══██╗██╔══██║░░░██║░░░██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║░░░░╚═══██╗╚═╝")
    print_with_delay(
        "╚█████╔╝╚█████╔╝██║░╚███║╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║░░░██████╔╝██╗")
    print_with_delay(
        "░╚════╝░░╚════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝░░░╚═════╝░╚═╝")
    print("")
    print_with_delay(
        "██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░██████╗░█████╗░░█████╗░██████╗░███████╗██████╗░  ██╗")
    print_with_delay(
        "╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██║")
    print_with_delay(
        "░╚████╔╝░██║░░██║██║░░░██║  █████╗░░╚█████╗░██║░░╚═╝███████║██████╔╝█████╗░░██║░░██║  ██║")
    print_with_delay(
        "░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██╔═══╝░██╔══╝░░██║░░██║  ╚═╝")
    print_with_delay(
        "░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗██████╔╝╚█████╔╝██║░░██║██║░░░░░███████╗██████╔╝  ██╗")
    print_with_delay(
        "░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═════╝░  ╚═╝")
    print_with_delay(YELLOW + "CREATED BY: TEAM ONE")
    print_with_delay(
        YELLOW + "ADEOLA, BRADLEY, FAZAL, PAYIKENE, MAZIAR, ZAMIR")
    print_with_delay(YELLOW + "THANK YOU" + RESET)

else:
    print_with_delay(YELLOW + BOLD + UNDERLINE +
                     "You hesitate to open the door and remain trapped in the haunting house.")
    print_with_delay("Game Over! Your adventure ends here.")
    playsound("Sounds/finallaugh.mp3", block=False)
    print("")
    print_with_delay(
        RED + "██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗")
    print_with_delay(
        RED + "██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗")
    print_with_delay(
        RED + "██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝")
    print_with_delay(
        RED + "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗")
    print_with_delay(
        RED + "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║")
    print_with_delay(
        RED + "╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝")
    print_with_delay(YELLOW + "CREATED BY: TEAM ONE")
    print_with_delay(
        YELLOW + "ADEOLA, BRADLEY, FAZAL, PAYIKENE, MAZIAR, ZAMIR")
    print_with_delay(YELLOW + "THANK YOU" + RESET)