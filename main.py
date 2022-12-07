import random
import os
import pyautogui as pe
import time

print("Welcome to the Random Agent Selector.")
time.sleep(3)
agents = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Fade", "Harbor", "Jett",
          "KAY/O", "KillJoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

number = random.randint(0, 19)
print("You are playing as " + agents[number] + ". Enjoy!")

if number == 0:  # Astra
    pe.click(579, 926)
    pe.click(989, 821)

if number == 1:  # Breach
    pe.click(666, 928)
    pe.click(989, 821)

if number == 2:  # Brim
    pe.click(744, 916)
    pe.click(989, 821)

if number == 3:  # Chamber
    pe.click(815, 922)
    pe.click(989, 821)

if number == 4:  # Cypher
    pe.click(902, 923)
    pe.click(989, 821)

if number == 5:  # fade
    pe.click(995, 923)
    pe.click(989, 821)


if number == 6:  # harbor
    pe.click(1104, 911)
    pe.click(989, 821)

if number == 7:  # Jett
    pe.click(1074, 926)
    pe.click(989, 821)

if number == 8:  # kayo
    pe.click(1168, 929)
    pe.click(989, 821)

if number == 9:  # kj
    pe.click(1236, 928)
    pe.click(989, 821)

if number == 10:  # neon
    pe.click(1326, 924)
    pe.click(989, 821)

if number == 11:  # omen
    pe.click(582, 1002)
    pe.click(989, 821)

if number == 12:  # phoenix
    pe.click(678, 1005)
    pe.click(989, 821)

if number == 13:  # raze
    pe.click(731, 1003)
    pe.click(989, 821)

if number == 14:  # reyna
    pe.click(821, 1006)
    pe.click(989, 821)

if number == 15:  # Sage
    pe.click(908, 1005)
    pe.click(989, 821)

if number == 16:  # skye
    pe.click(989, 1003)
    pe.click(989, 821)

if number == 17:  # sova
    pe.click(1075, 1001)
    pe.click(989, 821)

if number == 18:  # viper
    pe.click(1157, 1004)
    pe.click(989, 821)

if number == 19:  # yoru
    pe.click(1245, 1002)
    pe.click(989, 821)

time.sleep(5)
