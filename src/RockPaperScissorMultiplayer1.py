import random


# Printing the text in color provided by the user
def printingTextWithcolor(text, color):
    if color.lower() == "red":
        print("\x1b[0;30;41m"+text+"\x1b[0m")
    elif color.lower() == "green":
        print("\x1b[6;30;42m"+text+"\x1b[0m")
    elif color.lower() == "yellow":
        print("\x1b[0;30;43m"+text+"\x1b[0m")
    elif color.lower() == "blue":
        print("\x1b[0;30;46m"+text+"\x1b[0m")


# Play again module
def playAgain():
    while True:
        playagain = input(
            "Do you want to play again?\n1. Yes\t2. No\nYou can also put the name (Case Insensitive): ")
        # To remove the before and after spaces in the user supplied string
        playagain = playagain.strip()
        if playagain == "1" or playagain.lower() == "yes":
            break
        elif playagain == "2" or playagain.lower() == "no":
            quit()
        else:
            print("\nIncorrect option selected. Please select right option: ")

# Method to accept user inputs for the round


def takeUserInput(player):
    while True:
        playerOption = input(
            "\n"+player+" please select your option. Enter the number/text for the option.\n 1. ROCK \t 2. PAPER \t 3. SCISSOR: ")
        playerOption = playerOption.strip()
        if playerOption == "1" or playerOption.upper() == "ROCK":
            playerOption = "ROCK"
            break
        elif playerOption == "2" or playerOption.upper() == "PAPER":
            playerOption = "PAPER"
            break
        elif playerOption == "3" or playerOption.upper() == "SCISSOR":
            playerOption = "SCISSOR"
            break
        else:
            print("\n Please select correct option \n")
    return playerOption


# Method to determine the winner of the round
def roundWinner(opt1, opt2):
    if opt1 == "ROCK" and opt2 == "SCISSOR" or opt1 == "SCISSOR" and opt2 == "PAPER" or opt1 == "PAPER" and opt2 == "ROCK":
        return "Win"
    elif opt2 == "ROCK" and opt1 == "SCISSOR" or opt2 == "SCISSOR" and opt1 == "PAPER" or opt2 == "PAPER" and opt1 == "ROCK":
        return "Loss"
    else:
        return "Draw"


# Variables declaration needed for the game
x = y = z = 0
optionList = ["ROCK", "PAPER", "SCISSOR"]
welcomeText = "\n Welcome to the Game of ROCK-PAPER-SSCISSOR \n"
rules = "Following are the rules of the game:\n"+"1. Game will be consist of 3 rounds\n"+"2. Player can play against Computer or another player\n"+"2. For each round Player will select 1 option out of Rock/Paper/Scissor and the computer or Other Player will do the same\n" + "3. Each round there can 3 outputs Player wins/ Computer/Other Player wins/ Draw\n" + \
    "4. Winner will be declared at the end of the game depending upon the number of rounds won\n" + \
    "5. Also game will end if first two rounds are won by same player"
playerSelections = []
againstSelections = []

# Logic to play the game
while True:
    printingTextWithcolor(welcomeText, "yellow")
    printingTextWithcolor(rules, "blue")
    while True:
        against = input(
            "\nSelect an option to play against.\n1.Computer\t2.Player\t3.Logout: ")
        against = against.strip()
        if against == "1" or against.lower() == "computer":
            against = "COMPUTER"
            break
        elif against == "2" or against.lower() == "player":
            against = "PLAYER-2"
            break
        elif against == "3" or against.lower() == "logout":
            print("Goodbye!")
            quit()
        else:
            print("Incorrect option selected")

    while x+y+z < 3:
        playerOption = takeUserInput("PLAYER-1")
        playerSelections.append(playerOption)

        if against == "COMPUTER":
            againstOption = random.choice(optionList)
        else:
            againstOption = takeUserInput(against)

        againstSelections.append(againstOption)

        output = roundWinner(playerOption, againstOption)

        if output == "Win":
            print("\n"+playerOption+" beats the "+againstOption)
            winText = "PLAYER-1 won this round."
            printingTextWithcolor(winText, "green")
            x = x+1
            if x > 1:
                break
        elif output == "Loss":
            print("\n"+againstOption+" beats the "+playerOption)
            winText = against+" won this round."
            printingTextWithcolor(winText, "green")
            y = y+1
            if y > 1:
                break
        else:
            print("\n"+playerOption+" matches the "+againstOption)
            winText = "This round is a draw"
            printingTextWithcolor(winText, "yellow")
            z = z+1

    print("\n")
    if (x > y):
        winText = "PLAYER-1 is the winner of the game"
        printingTextWithcolor(winText, "green")
        winText = against+" Better luck next time"
        printingTextWithcolor(winText, "red")
    elif (y > x):
        winText = against+" is the winner of the game"
        printingTextWithcolor(winText, "green")
        winText = "PLAYER-1 Better luck next time"
        printingTextWithcolor(winText, "red")
    else:
        winText = "Its a Draw"
        printingTextWithcolor(winText, "yellow")

    print("\nGame Summary\n")
    print("PLAYER-1 selections were", playerSelections, "\n")
    print(against+" selections were", againstSelections, "\n")

    # Clearing the storing elements to allow user to lay again from start
    playerSelections.clear()
    againstSelections.clear()
    x = y = z = 0

    # Asking user to play again
    playAgain()
