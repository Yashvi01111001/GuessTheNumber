import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or quit (press Q):")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success!")
        break
    elif(userChoice < target):
        print("Your number is too small. Take a bigger guess...")
    else:   
        print("Your number is too large. Take a smaller guess...")
    
print("----GAME OVER----")