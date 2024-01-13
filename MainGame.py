print("Hello, welcome to Adventure Time! \nWhat is your going to be your Adventurer's Name?")
Username = input("Enter username: ")
print ("Your Adventurer's Name is: " + Username)
print ("Hello " + Username + ", I'm so glad that you're here! There is a dragon wrecking havoc on the city... Can you please us kill it?")
KillorNot = input ("Do you want to help your city's citizens kill the dragon? Y/N")

if KillorNot == "Y":
    print ("Oh thank you so much! The dragon is hiding in a secret lair under the town hall. You'll need some equipment first before you can take it on")
else:
    while KillorNot != "Y":
        print ("\nPlease help us kill the dragon, we really need you out there! We will compensate you greatly")
        KillorNot = input ("Do you want to help your city's citizens kill the dragon? Y/N")
        if KillorNot != "N" and KillorNot != "Y":
            print ("Please enter a valid input.")
             
        
print ("Oh thank you so much! The dragon is hiding in a secret lair under the town hall. You'll need some equipment first before you can take it on")

# elif KillorNot == "N":
#     print ("Please help us kill the dragon, we really need you out there! We will compensate you greatly")
#     KillorNot = input ("Do you want to help your city's citizens kill the dragon? Y/N ")
