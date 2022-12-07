# Release #: 1.10
# Patch Notes:
# Added the option to choose when to run the script. This enables the user to open the program while in queue or before queue and still be able to run the script when the game is found
# Added specific messages for each agent when picked
# Added the option to reroll at the end of the pick

import random
import pyautogui as pe
import time


def invalid_input():
    print("Invalid input. ")
    print("Terminating application")
    time.sleep(2)
    quit()


def random_agent():

    time.sleep(3)
    agents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Fade", "Harbor", "Jett",
              "KAY/O", "KillJoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

    number = random.randint(0, 19)
    print("You are playing as " + agents[number] + ". Enjoy!")

    if number == 0:  # Astra
        pe.click(582, 921)
        #pe.click(989, 821)

    if number == 1:  # Breach
        pe.click(673, 935)
        #pe.click(989, 821)

    if number == 2:  # Brim
        pe.click(743, 922)
        #pe.click(989, 821)

    if number == 3:  # Chamber
        pe.click(834, 927)
        #pe.click(989, 821)

    if number == 4:  # Cypher
        pe.click(926, 915)
        #pe.click(989, 821)

    if number == 5:  # fade
        pe.click(1006, 936)
        #pe.click(989, 821)

    if number == 6:  # harbor
        pe.click(1097, 929)
        #pe.click(989, 821)

    if number == 7:  # Jett
        pe.click(1172, 929)
        #pe.click(989, 821)

    if number == 8:  # kayo
        pe.click(1172, 929)
        #pe.click(989, 821)

    if number == 9:  # kj
        pe.click(1332, 924)
        #pe.click(989, 821)

    if number == 10:  # neon
        pe.click(573, 1000)
        #pe.click(989, 821)

    if number == 11:  # omenn
        pe.click(668, 1013)
        #pe.click(989, 821)

    if number == 12:  # phoenix
        pe.click(759, 1011)
        #pe.click(989, 821)

    if number == 13:  # raze
        pe.click(837, 1004)
        #pe.click(989, 821)

    if number == 14:  # reyna
        pe.click(929, 1012)
        #pe.click(989, 821)

    if number == 15:  # Sage
        pe.click(993, 1011)
        #pe.click(989, 821)

    if number == 16:  # skye
        pe.click(993, 1011)
        #pe.click(989, 821)

    if number == 17:  # sova
        pe.click(1164, 1008)
        #pe.click(989, 821)

    if number == 18:  # viper
        pe.click(1256, 1004)
        #pe.click(989, 821)

    if number == 19:  # yoru
        pe.click(1326, 1008)
        #pe.click(989, 821)

    reroll_choice = input("Would you like to reroll? y/n \n")
    if reroll_choice == "y" or reroll_choice == "yes" or reroll_choice == "":
        random_agent()
    else:
        print("Terminating application in 3 seconds.")
        time.sleep(3)


print("Welcome to the Random Agent Selector")
time.sleep(2)

firstinput = input("Would you like to proceed? (y/n) \n").lower()
if firstinput == "y" or firstinput == "yes" or firstinput == "":
    time.sleep(1)
    random_agent()
elif firstinput == "n" or firstinput == "no":
    print("Terminating application...")
    pe.sleep(2)
    quit()
else:
    invalid_input()
