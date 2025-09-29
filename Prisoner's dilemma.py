import random
userpoints = 0
computerpoints = 0
extrauserpoints = 0
extracomputerpoints = 0

def choose():
    textchoice = input("would you like to Co-operate (a) or Defect (d)")
    if textchoice == "a":
        choice = True
    elif textchoice == "d":
        choice = False
    else:
        print("invalid choice, please type \"a\" or \"d\"")
        return choose()
    return choice
def givepoints(choice1, choice2):
    if (choice1 == True and choice2 == True):
        print("you both co-operated well done")
        return (3, 3)
    elif (choice1 == False and choice2 == True):
        print("you defected and the computer co-operated, well done!!")
        return (5, 0)
    elif (choice1 == True and choice2 == False):
        print("you co-operated and the computer defected, unlucky")
        return (0, 5)
    elif (choice1 == False and choice2 == False):
        print("you both defected, unlucky")
        return (1, 1)
    else:
        print("Game error?")





#MAIN GAME LOOP

while True:
    choice1 = choose()
    if random.randint(1,2) == 1:
        computerchoice = True
    else:
        computerchoice = False
    extrauserpoints, extracomputerpoints = givepoints(choice1, computerchoice)
    userpoints += extrauserpoints
    computerpoints += extracomputerpoints
    print("You have", userpoints, "and the computer has", computerpoints)

    
