print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************''')
print("Welcome to the Game of GUTS")
choice1=input('You are on a road somewhere in a forest & you see a board saying "Danger ahead" would you still go ahead? yes or no: ').lower()
if choice1=="no":
   choice2= input('''\nIts dark & cold out here & you can see light coming from a house 500m away. would you like to take shelter? yes or no: ''').lower()
   
   if choice2=="yes":
      choice3=input('''\nKnock! knock! an old lady opened the door with a knife smiling at you.\n"kill" or "Run"''').lower()
      
      if choice3=="kill":
         print('''\nYou saw chopped onions & realised she was not going to attack\nYou decide to sleep.''')
         
         choice4=input('\ntring tring, its morning wanna wake up? "yes" or "no"?: ').lower()
         if choice4=="yes":
            print("\nIt was all a Dream")
         else:
            print("\nThe old lady's husband came back & saw his wife dead he killed you")

      else:
         print("\nDude go play subway surfer if you are this coward")
   else:
     print("\nIts a game of Guts, you died because you are not brave enough")
else:
    print("\nThere's a Board saying danger ahead, only a fool will go ahead\nYou are dead because of stupidity.")
