import random

randomNum = random.randint(1, 100)

while True:
    userInput = input("Guess the number or Quit :")
    if(userInput == "Quit" or userInput == "quit"):
        break

    userInput = int(userInput)
    if(userInput == randomNum):
        print("Success: Correct Guess!!")
        break
    elif(userInput < randomNum):
        print("your number  was to small. Take a bigger guess..")
    else:
        print("your number  was to big. Take a smaller guess..")


print("------GAME OVER-------")