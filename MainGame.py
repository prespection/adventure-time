import time
inventory = []
weaponchoice1 = "fork"
weaponchoice2 = "spoon"
weaponchoice3 = "sword"
weaponchoice4 = "all"
weaponchoice5 = "everything"
DragonHP = 100

print("Hello, welcome to Adventure Time!\nWhat is going to be your Adventurer's Name?")
Username = input("Enter username: ")
print("Your Adventurer's Name is: " + Username)

print("Hello " + Username + ", I'm so glad that you're here! There is a dragon wreaking havoc on the city..."
      "Can you please help us kill it?")
KillorNot = input("Do you want to help your city's citizens kill the dragon? Y/N: ")

if KillorNot == "Y":
    print("Oh thank you so much! The dragon is hiding in a secret lair under the town hall. You'll need some equipment "
          "first before you can take it on")
    time.sleep(2)
    print("\nOkay, we don't have much, so we'll have to work with what we've got.... ")
    time.sleep(2)
    Weapon = input("\nI've got a fork, a spoon, and a sword... Which one would you like to fight the dragon? or... do you want them all? ")
else:
    while KillorNot != "Y":
        if KillorNot != "N" and KillorNot != "Y":
            print("Please enter a valid input.")
        print("\nPlease help us kill the dragon, we really need you out there! We will compensate you greatly")
        KillorNot = input("Do you want to help your city's citizens kill the dragon? Y/N: ")

    # if the player decides to help, the code will continue here
    print("Oh thank you so much! The dragon is hiding in a secret lair under the town hall. You'll need some equipment "
          "first before you can take it on")
    time.sleep(2)
    print("\nOkay, we don't have much, so we'll have to work with what we've got.... ")
    time.sleep(2)
    Weapon = input ("\nI've got a fork, a spoon, and a sword... Which one would you like to fight the dragon? or... do you want them all? ")
    time.sleep(1)

WhichWeapon = Weapon.lower()  
while not (weaponchoice1 in WhichWeapon or weaponchoice2 in WhichWeapon or weaponchoice3 in WhichWeapon or weaponchoice4 in WhichWeapon):
    print("You need to select a weapon, we cannot do empty handed!")
    time.sleep(1)
    Weapon = input ("Do you want a fork, a spoon, a sword or everything?")
    WhichWeapon = Weapon.lower()

time.sleep(1)
   
if weaponchoice1.lower() in WhichWeapon:
    inventory.append("Fork")
    print("\nThe fork... interesting choice. We'll make a meal out of this dragon!")
elif weaponchoice2.lower() in WhichWeapon:
    inventory.append("Spoon")
    print("\nThe spoon... really? Okay, if you say so!")
elif weaponchoice3.lower() in WhichWeapon:
    inventory.append("Sword")
    print("\nI always knew that you were a warrior! Here's your sword")
elif weaponchoice4.lower() in WhichWeapon:
    inventory.append("Spoon, Fork, Sword")
    print("\nI like the way you think... Let's take everything we have and kill this dragon!")
elif weaponchoice5.lower() in WhichWeapon:
    inventory.append("Spoon, Fork, Sword")
    print("\nI like the way you think... Let's take everything we have and kill this dragon!")    

time.sleep (3)

print("\nThe entrance to the townhall is this way, come on!")
time.sleep(3)
print("\n*You enter the townhall and an eternal abyss rushes past the entrance*")
time.sleep(3)
print("\nWait...")
time.sleep(3)
print("\nDid you feel that...?")
time.sleep(3)
print("\nI think the dragon is nearby!!")
time.sleep(3)
print("\n*You see a large door that's been busted open in the distance...*")
time.sleep(3)
print("\nHEY! THAT DOOR LEADS TO THE UNDERGROUND... THE DRAGON MUST BE THERE... LETS GO SLAY IT")
time.sleep(3)
print("\n*You decent down and see a large creature sleeping...*")
time.sleep(3)
print("\nShhhh its the dragon... let's take it by surpirse")
print("Dragon's Health: " + str(DragonHP))

Action1 = input("\nDo you want to attack the dragon? Y or N: ") 

if Action1 == "Y":
    print("\nLETS ATTACK!!!!")
    time.sleep(2)
    print("\nWOW THAT WAS A SOLID STRIKE WARRIOR... I THINK YOU HURT IT")
    time.sleep(2)
    print("Dragon's Health: " + str(DragonHP-50))
    time.sleep(2)
    print ("\nOh no... I think its awake")
    time.sleep(3)
    print ("\n*The dragon awaken and swipes his tail knocking you and your friends down*")
    time.sleep(2)
else:
    while Action1 != "Y":
        if Action1 != "N" and Action1 != "Y":
            print ("\nPlease enter a valid input.")
        print ("\nThe dragon is sleeping this is our best chance to attack!")
        Action1 = input("\nDo you want to attack the dragon? Y or N: ") 
    print("\nLETS ATTACK!!!!")
    time.sleep(2)
    print("\nWOW THAT WAS A SOLID STRIKE WARRIOR... I THINK YOU HURT IT")
    time.sleep(2)
    print("Dragon's Health: " + str(DragonHP-50))
    time.sleep(2)
    print ("\nOh no... I think its awake")
    time.sleep(3)
    print ("\n*The dragon awaken and swipes his tail knocking you and your friends down*")
    time.sleep(2)

actionchoice1 = "fight"
actionchoice2 = "run"
Action2 = input("\nUUUGGGGGH.... Guys.... We have to get up... Do you get up and fight or do you run?")

Whichaction = Action2.lower()  
while not (actionchoice1 in Whichaction or actionchoice2 in Whichaction):
    Action2 = input("This is not the time to blabber... We need to choose: Fight or Run: ")
    Whichaction = Action2.lower()
time.sleep(1)

if actionchoice1.lower() in Whichaction:
    print("\nI knew you were a true warrior! LET'S ATTACK AGAIN!!!!!!")
    time.sleep(3)
    print("\n*You and your friends find the will to stand up and give one final blow through the dragon's heart*")
    time.sleep(3)
    print("Dragon's Health: " + str(DragonHP-100))
    time.sleep(3)
    print("\nWE DID IT!!! WE SLAYED THE DRAGON! THANK YOU SO MUCH WARRIOR")
    time.sleep(3)
    print("\nCongratulations! You beat adventure time, you are a true warrior")
elif actionchoice2.lower() in Whichaction:
    print("\nYou're right... There is no way we can kill this dragon when we're this hurt... we have to run")
    time.sleep(3)
    print("\n*You and your friend run away from the dragon's lair before it attacks you*")
    time.sleep(3)
    print("\nWe'll come back to fight another time... The dragon is too strong for us right now...")
    time.sleep(3)
    print("\nGAME OVER....")