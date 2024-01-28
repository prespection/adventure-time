import time
inventory = []
weaponchoice1 = "fork"
weaponchoice2 = "spoon"
weaponchoice3 = "sword"
weaponchoice4 = "all"

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
