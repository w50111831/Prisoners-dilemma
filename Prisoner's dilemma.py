import random
userpoints = 0
computerpoints = 0
extrauserpoints = 0
extracomputerpoints = 0

def pick_strategy():
    print("Choose the computer's strategy")
    print("1:Random")
    print("2:defect")
    print("3:cooperate")
    print("4:copyuser")
    strategy = input("Enter choice 1-4")
    return strategy


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

def computer_move(strategy, choice1):
    if strategy == "1":
        if random.randint(1,2) == 1:
            computerchoice = True
        else:
            computerchoice = False
    if strategy == "2":
        computerchoice = False
    if strategy == "3":
        computerchoice = True
    if strategy == "4":
        computerchoice = choice1
    return computerchoice


strategy = pick_strategy()

#MAIN GAME LOOP
while True:
    choice1 = choose()
    computerchoice = computer_move(strategy, choice1)
    extrauserpoints, extracomputerpoints = givepoints(choice1, computerchoice)
    userpoints += extrauserpoints
    computerpoints += extracomputerpoints
    print("You have", userpoints, "and the computer has", computerpoints)

    
