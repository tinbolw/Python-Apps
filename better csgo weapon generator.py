Terrorist = False
Counter_Terrorist = False
money = 0
teamchecker = 0
Casual = False
kevlar = 0
helmet = 0
defuse_kit = 0
if_casual = 0
team = input("What team are you on? ")
while teamchecker == 0:
    if team == "Counter Terrorist" or team == "CT":
        Counter_Terrorist = True
        teamchecker += 1
    elif team == "Terrorists" or team == "T" or team == "Terrorist":
        Terrorist = True
        teamchecker += 1
    else:
        print("Not a valid team")
        teamchecker += 2

if teamchecker == 1:
    if_casual = input("Are you playing casual? (Y/N) ")

if if_casual = "Y":
    Casual = True
else:
    Casual = False

if teamchecker == 1:
    money = float(input("How much money do you have? "))

if teamchecker == 1 and not(Casual):
    kevlar = input("Do you want to buy kevlar? (Y/N) ")

if teamchecker == 1 and not(Casual):
    helmet = input("Do you want to buy a helmet? (Y/N) ")

if helmet == "Y" and not(Casual):
    money += 350

if kevlar = "Y" and not(Casual):
    money += 650

if Counter_Terrorist and not(Casual):
    defuse_kit = input("Do you want to buy a defuse kit? (Y/N) ")

if defuse_kit == "Y":
    money += 200

if teamchecker == 1:
    grenades = input("Do you want to buy grenades? (Y/N) ")

if grenades == "Y":


if money <=


if teamchecker == 2:
    quit












