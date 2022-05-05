import random as r


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
    elif color.lower() == "purple":
        print("\x1b[0;30;45m"+text+"\x1b[0m")


# Display Game Data
def displayGameData(d):
    for k, v in d.items():
        if isinstance(v[0], list):
            for i in range(0, 2, 1):
                print("\x1b[0;30;46m", k, "Round-", i+1, v[i],
                      "Total -", totalCount(v[i]), "\x1b[0m", end=" ")
        else:
            print("\x1b[0;30;46m", k, v, "Total -",
                  totalCount(v), "\x1b[0m", end=" ")

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
            text = "\nIncorrect option selected. Please select right option: "
            printingTextWithcolor(text, "red")


# Drawing a card from the Deck
def cardDraw(cardDeckList, userList):
    card = r.choice(cardDeckList)
    cardDeckList.remove(card)
    userList.append(card)


# Getting sum of the cards
def totalCount(userList):
    sum = 0
    count = 0
    for val in userList:
        value = 0
        if val[0] == "T" or val[0] == "J" or val[0] == "Q" or val[0] == "K":
            value = 10
        elif val[0] == "A":
            count = count + 1
        else:
            value = int(val[0])
        sum = value + sum
    # Handling the Ace situation
    if sum <= 10 and count > 1 and sum+10+count <= 21:
        sum = sum + count + 10
    elif sum <= 10 and count > 1 and sum+10+count > 21:
        sum = sum + count
    elif sum > 10 and count > 1:
        sum = sum + count
    elif sum <= 10 and count == 1:
        sum = sum + 11
    elif sum > 10 and count == 1:
        sum = sum + count
    return sum


def deckCreation(cardDeckList, num):
    for i in range(0, num, 1):
        for val1 in string1:
            for val2 in tuple:
                item = val1+val2
                cardDeckList.append(item)


# Variable declaration
cardDeckList = []
string1 = "A23456789TJQK"
#string1 = "AJQK12"
tuple = ("S", "D", "H", "F")
dictData = {"Dealer": []}
playerList = []
bjListStatus = {}
amountDict = {}
welcomeText = "\n Welcome to the Game of BLACK JACK \n"
rules = "Following are the rules of the game:\n"+"1. User will be asked how many players ae playing the game\n"+"2. Upon selection every player has to put a bet.(By default every player is assigned with $50) \n"+"3. After putting bet all player will be assigned 2 cards to players and 1 to dealer (All player can see dealer and other player cards)\n" + "4. Every player will get a turn to get more cards or can stay\n" + \
    "5. Player can split the turn if they get same cards in first attempt\n" + \
    "6. After all players done playing dealer will play\n" + \
        "7. After dealers turn result will be displayed (If player hits Black Jack (Exact 21 count) they will get 3 times the betted amount. If player is busted (count>21) they will loose betted amount. If player count is less than 21 but greater than count of dealer they will get double the betted amount)"

printingTextWithcolor(welcomeText, "yellow")
printingTextWithcolor(rules, "blue")
print("\n")
while True:
    userInput = input("Enter number of player playing: ")
    userInput = userInput.strip()
    if userInput.isdigit() and int(userInput) > 0:
        break
    else:
        print("Please enter only numbers greater than 0")

print("\n")

for i in range(1, int(userInput)+1, 1):
    playerValue = "Player-"+str(i)
    #dictData[playerValue] = []
    playerList.append(playerValue)
    amountDict[playerValue] = []
    amountDict[playerValue].append(50)

while True:

    # Creating a deck of cards no of player X deck
    deckCreation(cardDeckList, int(userInput))

    for player in playerList:
        dictData[player] = []
        while True:
            betAmount = input(
                "\x1b[3;30;47m"+player+" enter amount to bet (Amount should be whole number and Minimum bet amount is $5):"+"\x1b[0m")
            betAmount = betAmount.strip()
            if betAmount.isnumeric() and int(betAmount) < amountDict[player][0] and int(betAmount) >= 5:
                if len(amountDict[player]) >= 2:
                    amountDict[player][1] = int(betAmount)
                else:
                    amountDict[player].append(int(betAmount))
                amountDict[player][0] = amountDict[player][0] - int(betAmount)
                break
            else:
                print(
                    "Either incorrect amount is entered or amount entered is greater than amount you have. You have "+str(amountDict[player][0])+" in your wallet.")

    print("\n")
    # Assigning two random cards to the player
    for key, val in dictData.items():
        if key != "Dealer":
            cardDraw(cardDeckList, dictData[key])
            cardDraw(cardDeckList, dictData[key])
        else:
            cardDraw(cardDeckList, dictData[key])

    for player in playerList:
        #print("\x1b[0;30;46m", dictData, "\x1b[0m")
        displayGameData(dictData)
        print("\n")
        bjListStatus[player] = []
        if dictData[player][0][0] == dictData[player][1][0]:
            while True:
                splitInput = input(
                    "\x1b[3;30;47m"+"\nDo you want to split?\n1.Yes\t2.No : "+"\x1b[0m")
                if splitInput == "1":
                    if amountDict[player][0] >= amountDict[player][1] * 2:
                        val1 = dictData[player][0]
                        val2 = dictData[player][1]
                        dictData[player] = [[], []]
                        dictData[player][0].append(val1)
                        dictData[player][1].append(val2)
                        bjListStatus[player] = [[], []]
                        amountDict[player][1] = amountDict[player][1] * 2
                        amountDict[player][0] = amountDict[player][0] - \
                            amountDict[player][1]/2
                        break
                    else:
                        print(
                            player+" does not have enough money to split. Normal game will continue.")
                        break
                elif splitInput == "2":
                    break
                else:
                    printingTextWithcolor(
                        "Incorrect Option selected.\n", "red")
                    #print("Incorrect option")

        if isinstance(dictData[player][0], list):
            for i in range(0, 2, 1):
                print(player+" round-", i+1, " begins.\n")
                while True:
                    if totalCount(dictData[player][i]) > 21:
                        #print("\x1b[0;30;46m", dictData, "\x1b[0m")
                        displayGameData(dictData)
                        print("\n")
                        text = player+"- busted in round "+str(i+1)
                        print("\n")
                        printingTextWithcolor(text, "red")
                        bjListStatus[player][i].append("Busted")
                        break
                    elif totalCount(dictData[player][i]) == 21:
                        #print("\x1b[0;30;46m", dictData, "\x1b[0m")
                        displayGameData(dictData)
                        print("\n")
                        text = player+" hit Black Jack for round " + \
                            str(i+1)+"\n"
                        printingTextWithcolor(text, "green")
                        bjListStatus[player][i].append("BlackJack")
                        break
                    playInput = input("\n"+"\x1b[3;30;47m" +
                                      player+"-Do you want to hit or Stay?\n1.Hit\t2.Stay: "+"\x1b[0m")
                    if playInput == "1":
                        cardDraw(cardDeckList, dictData[player][i])
                        #print("\x1b[0;30;46m", dictData, "\x1b[0m")
                        displayGameData(dictData)
                        print("\n")
                        print("\x1b[0;30;43m"+"Player Cards:",
                              player, dictData[player][i], " Total: ", totalCount(dictData[player][i]), "\x1b[0m")
                    elif playInput == "2":
                        bjListStatus[player][i].append("Normal")
                        break
                    else:
                        printingTextWithcolor(
                            "Incorrect option is selected\n", "red")
        else:
            while True:
                if totalCount(dictData[player]) > 21:
                    #print("\x1b[0;30;46m", dictData, "\x1b[0m")
                    displayGameData(dictData)
                    text = player+"is busted"
                    print("\n")
                    printingTextWithcolor(text, "red")
                    print("\n")
                    bjListStatus[player].append("Busted")
                    break
                elif totalCount(dictData[player]) == 21:
                    #print("\x1b[0;30;46m", dictData, "\x1b[0m")
                    displayGameData(dictData)
                    text = player+" hit Black Jack"
                    print("\n")
                    printingTextWithcolor(text, "green")
                    print("\n")
                    bjListStatus[player].append("BlackJack")
                    break
                playInput = input("\n"+"\x1b[3;30;47m" +
                                  player+"-Do you want to hit or Stay?\n1.Hit\t2.Stay: "+"\x1b[0m")
                if playInput == "1":
                    cardDraw(cardDeckList, dictData[player])
                    #print("\x1b[0;30;46m", dictData, "\x1b[0m")
                    displayGameData(dictData)
                    print("\n")
                    print("\x1b[0;30;43m"+"Player Cards:",
                          player, dictData[player], " Total: ", totalCount(dictData[player]), "\x1b[0m")
                elif playInput == "2":
                    bjListStatus[player].append("Normal")
                    break
                else:
                    printingTextWithcolor(
                        "Incorrect option is selected", "red")

    #print("\x1b[0;30;46m", dictData, "\x1b[0m")
    displayGameData(dictData)
    print("\n")
    print("\nDealers turn to Play:")

    while True:
        if totalCount(dictData["Dealer"]) > 21:
            #print("\x1b[0;30;46m", dictData, "\x1b[0m")
            displayGameData(dictData)
            print("\n")
            print("\x1b[0;30;43m"+"Dealer Cards:",
                  dictData["Dealer"], "\x1b[0m")
            break
        elif totalCount(dictData["Dealer"]) == 21:
            #print("\x1b[0;30;46m", dictData, "\x1b[0m")
            displayGameData(dictData)
            print("\n")
            print("\x1b[0;30;43m"+"Dealer Cards:",
                  dictData["Dealer"], "\x1b[0m")
            print("\n")
            break
        playInput = input(
            "\n"+"\x1b[3;30;47m"+"Do you want to hit or Stay?\n1.Hit\t2.Stay: "+"\x1b[0m")
        if playInput == "1":
            cardDraw(cardDeckList, dictData["Dealer"])
            #print("\x1b[0;30;46m", dictData, "\x1b[0m")
            displayGameData(dictData)
            print("\n")
            print("\x1b[0;30;43m"+"Dealer Cards:",
                  dictData["Dealer"], " Total: ", totalCount(dictData["Dealer"]), "\x1b[0m")
        elif playInput == "2":
            break
        else:
            printingTextWithcolor("Incorrect option is selected", "red")
    print("\n")
    print("-----------------------------------GAME RESULTS-------------------------------------------------")
    for player in playerList:
        if isinstance(dictData[player][0], list):
            for i in range(0, 2, 1):
                if bjListStatus[player][i][0] != "Busted" and bjListStatus[player][i][0] != "BlackJack" and totalCount(dictData["Dealer"]) <= 21:
                    if totalCount(dictData["Dealer"]) > totalCount(dictData[player][i]):
                        text = player+" lost to dealer in round" + \
                            str(i+1) + \
                            ". Amount Lost" + \
                            str(amountDict[player][1]/2) + \
                            ". Amount Remaining"+str(amountDict[player][0])
                        printingTextWithcolor(text, "red")
                    elif totalCount(dictData["Dealer"]) < totalCount(dictData[player][i]):
                        amountDict[player][0] = amountDict[player][0] + \
                            amountDict[player][1]
                        text = player + \
                            " won against the dealer in round" + \
                            str(
                                i+1)+". Amount Won: $"+str(amountDict[player][1]/2)+" Amount Remaining: $"+str(amountDict[player][0])
                        printingTextWithcolor(text, "green")
                    else:
                        amountDict[player][0] = amountDict[player][0] + \
                            amountDict[player][1]/2
                        text = player + \
                            " draws against the dealer in round-" + \
                            str(i +
                                1)+" Amount Remaining: $"+str(amountDict[player][0])
                        printingTextWithcolor(text, "yellow")
                elif bjListStatus[player][i][0] == "BlackJack":
                    amountDict[player][0] = amountDict[player][0] + \
                        amountDict[player][1] * 3/2
                    text = player+" already hit the Black Jack." + \
                        player+" beats the dealer in round-" + \
                        str(i+1)+". Amount Won: $"+str(
                            amountDict[player][1])+" Amount Remaining: $" + str(amountDict[player][0])
                    printingTextWithcolor(text, "green")
                elif bjListStatus[player][i][0] == "Busted":
                    # amountDict[player][0]
                    text = player+" already been Busted." + \
                        player+" lost to the dealer in round-" + \
                        str(
                            i+1)+". Amount Lost: $"+str(amountDict[player][1]/2) + ". Amount Remaining: $"+str(amountDict[player][0])
                    printingTextWithcolor(text, "red")
                else:
                    amountDict[player][0] = amountDict[player][0] + \
                        amountDict[player][1]
                    text = "Dealer has been busted."+player + \
                        " has won against the dealer in the round-" + \
                        str(i+1) + \
                        ". Amount Won: $" + \
                        str(amountDict[player][1]/2) + \
                        " Amount Remaining: $"+str(amountDict[player][0])
                    printingTextWithcolor(text, "green")
        else:
            if bjListStatus[player][0] != "Busted" and bjListStatus[player][0] != "BlackJack" and totalCount(dictData["Dealer"]) <= 21:
                if totalCount(dictData["Dealer"]) > totalCount(dictData[player]):
                    text = player+" lost to dealer." + \
                        ". Amount Lost: $" + \
                        str(amountDict[player][1]) + \
                        ". Amount Remaining: $"+str(amountDict[player][0])
                    printingTextWithcolor(text, "red")
                elif totalCount(dictData["Dealer"]) < totalCount(dictData[player]):
                    amountDict[player][0] = amountDict[player][0] + \
                        amountDict[player][1] * 2
                    text = player+" won against the dealer." + \
                        ". Amount Won: $" + \
                        str(amountDict[player][1]) + \
                        " Amount Remaining: $"+str(amountDict[player][0])
                    printingTextWithcolor(text, "green")
                else:
                    amountDict[player][0] = amountDict[player][0] + \
                        amountDict[player][1]
                    text = player+" draws against the dealer." + \
                        " Amount Remaining: $"+str(amountDict[player][0])
                    printingTextWithcolor(text, "yellow")
            elif bjListStatus[player][0] == "BlackJack":
                amountDict[player][0] = amountDict[player][0] + \
                    amountDict[player][1] * 3
                text = player+" already hit the Black Jack." + player+" beats the dealer" + ". Amount Won: $" + \
                    str(amountDict[player][1] * 2) + \
                    " Amount Remaining: $" + str(amountDict[player][0])
                printingTextWithcolor(text, "green")
            elif bjListStatus[player][0] == "Busted":
                text = player+" already been Busted." + player+" lost to the dealer"+". Amount Lost: $" + \
                    str(amountDict[player][1]) + \
                    ". Amount Remaining: $"+str(amountDict[player][0])
                printingTextWithcolor(text, "red")
            else:
                amountDict[player][0] = amountDict[player][0] + \
                    amountDict[player][1] * 2
                text = "Dealer has been busted."+player + " has won against the dealer"+". Amount Won: $" + \
                    str(amountDict[player][1]) + \
                    " Amount Remaining: $"+str(amountDict[player][0])
                printingTextWithcolor(text, "green")
    print("------------------------------------------------------------------------------------------------")
    print("\n")
    playAgain()
    bjListStatus.clear()
    cardDeckList.clear()
    dictData = {"Dealer": []}
