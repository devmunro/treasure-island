print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
action = input("Do you go ashore on the north side of island, Y or N? ")
if action == "Y":
    action = input("Do you enter the Village you see, Y or N? ")
    if action == "Y":
        print("The villagers cook you alive")
    else:
        print("You are safe")
        action = input("Do you go to the cave or the forest? cave or forest? ")
        if action == "cave":
            print("you enter the dark cave")
            action = input("Do you go left or right tunnel? left or right? ")
            if action == "left":
                print("You are attacked by a bear")
            else:
                print("You find the treasure")
        else:
            print("you got lost and was never seen again") 
else:
    action = input("do you enter the dark cave, Y or N? ")
    if action == "N":
        print("You are attacked by a bear")
    else:
        print("you enter the dark cave")
        action = input("Do you go left or right tunnel? left or right? ")
        if action == "left":    
            print("You are attacked by a bear")
        else:
            print("You find the treasure")

