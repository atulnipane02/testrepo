
# Method to display the summary of the quiz
def Summary(questionList, playerQuestionReponseList, questionAnswerList, num):
    print("\033[1m"+"\n Summary of the Trivia \n"+"\033[0m")
    for i in range(0, len(questionList[num])):
        if playerQuestionReponseList[i] == questionAnswerList[num][i]:
            print("\x1b[6;30;42m"+"\n Question "+str(i+1)+" - "+questionList[num][i]+"\n Selected Option - " +
                  playerQuestionReponseList[i]+"\n Correct Option - "+questionAnswerList[num][i]+"\n"+"\x1b[0m")
        else:
            print("\x1b[0;30;41m"+"\n Question "+str(i+1)+" - "+questionList[num][i]+"\n Selected Option - " +
                  playerQuestionReponseList[i]+"\n Correct Option - "+questionAnswerList[num][i]+"\n"+"\x1b[0m")


# Method to display correct ot incorrect selection of the question.
def QuestionCategory(questionList, optionsList, questionAnswerList, playerQuestionReponseList, num, playerCount):
    for i in range(0, len(questionList[num])):
        print(questionList[num][i])
        values = optionsList[num][i]
        print("Your options are (Select the number)")

        while True:
            val2 = input("\n1."+values[0]+" 2."+values[1] +
                         " 3."+values[2]+" 4."+values[3]+"\n\n")
            val2 = val2.strip()
            if val2 == "1":
                playerQuestionResponse = values[0]
                break
            elif val2 == "2":
                playerQuestionResponse = values[1]
                break
            elif val2 == "3":
                playerQuestionResponse = values[2]
                break
            elif val2 == "4":
                playerQuestionResponse = values[3]
                break
            else:
                print("\n Please select correct option \n")

        if playerQuestionResponse == questionAnswerList[num][i]:
            print("\x1b[6;30;42m" +
                  "\n Congratulations. You got the right answer \n"+"\x1b[0m")
            playerCount = playerCount + 1
        else:
            print("\x1b[0;30;41m" +
                  "\n Sorry, you selected incorrect option \n"+"\x1b[0m")

        playerQuestionReponseList.append(playerQuestionResponse)

    return playerCount


# Variable declaration to define questions, options and answers
questionList = [["Which among following is not a Country?", "Which of the following is the second lagest ocean?",
                 "What is the Capital of Florida state in USA?", "Which is the longest river in the world?", "Which is the tallest mountain in the world?"],
                ["What Was the Largest Contiguous Empire in History?",
                 "Who Discovered America?", "What Does the D in D-Day Stand For?", "When Was Russia’s “Red October” Revolution?", "Who Invented the Automobile?"],
                [" In feet, how high above the floor is the hoop on a basketball court?",
                 "What is the name of the Test cricket ground in Birmingham?", "What is the lowest score that cannot be scored with a single dart?", "What is the maximum length in inches of a baseball bat, to within 2 inches either way?", "How long is a ten-pin bowling lane in feet?"],
                ["Who was the very first American Idol winner?",
                 "Before Miley Cyrus recorded “Wrecking Ball,” it was offered to which singer?", "What was Madonna‘s first top 10 hit?", "What artists made up the supergroup The Traveling Wilburys?", "Which member of the Avengers had a brief stint as a pop star?"],
                ["How much percentage of the human body is constituted by water?", "At what rate does an average human being sneeze (miles/hour)?", "In which part of the human body do the smallest bones occur?", "How many taste buds does our tongue comprise of?", "Which is the largest organ in our body?"]]

optionsList = [
    [["Benin", "Cook Islands", "Cyprus", "Indio"],
     ["Arctic", "Indian", "Atlantic", "Pacific"],
     ["Miami", "Tampa", "Tallahassee", "Orlando"],
     ["Nile", "Amazon", "Lena", "Yellow River"],
     ["K2", "Makalu", "Mt Everest", "Lhotse"]],

    [["British", "Mongol", "Qing", "Russia"],
     ["Christopher Columbus", "Vasco da Gama",
        "Thomas Wyndham", "Antonio de Abreu"],
     ["Decision", "Death", "Designated", "Day"],
     ["1920", "1917", "1918", "1919"],
     ["Nicolas-Joseph Cugnot", "Robert Anderson", "George Baldwin Selden", "Karl Benz"]],

    [["8", "9", "10", "11"],
     ["Oval", "Lords", "Edgbaston", "Gabba"],
     ["23", "19", "25", "17"],
     ["39", "40", "41", "42"],
     ["40", "50", "60", "70"]],

    [["Lee DeWyze", "Kelly Clarkson", "Fantasia Barrino", "Ruben Studdard"],
     ["Alice Cooper", "Beyoncé", "Ariana", "Britney Spears"],
     ["Holiday", "Bitch I’m Madonna", "God Control", "Nobody Knows Me"],
     ["George Harrison", "Roy Orbison", "Jeff Lynne", "All of the above"],
     ["Scarlett Johanson", "Brie Larson", "Elizabeth Olsen", "Natalie Portman"]],

    [["50", "66", "75", "85"],
     ["75", "90", "100", "110"],
     ["Nose", "Finger", "Ears", "Toes"],
     ["5000", "7000", "9000", "10000"],
     ["Brain", "Liver", "Skin", "Pancreas"]]
]

questionAnswerList = [["Indio", "Atlantic",
                       "Tallahassee", "Nile", "Mt Everest"],
                      ["Mongol", "Christopher Columbus",
                       "Day", "1917", "Karl Benz"],
                      ["10", "Edgbaston", "23", "42", "60"],
                      ["Kelly Clarkson", "Beyoncé",
                       "Holiday", "All of the above", "Brie Larson"],
                      ["66", "100", "Ears", "9000", "Skin"]]

playerQuestionReponseList = []
playerCount = 0

while True:
    print("\n Welcome to the game of Trivia ")
    print("\x1b[0;30;43m" +
          "\n Welcome to the Game of TRIVIA \n"+"\x1b[0m")

    print("\x1b[0;30;46m"+"Following are the rules of the game:\n"+"1. Game will be consist of 5 Questions\n"+"2. Player can select the Category for the Quiz\n" +
          "3. For every question player gets 1 point\n"+"4. After attempting a question player will be indicated whether selected option is correct or not \n"+"5. At the endd of the Quiz a summary will be displayed for Player peerfomance\n"+"6. Player can continue playing the quiz by selecting the option at the eend of the Quiz "+"\x1b[0m")

    while True:
        val = input(
            "\n Select you category. Enter the number or text for the option.\n 1. GEOGRAPHY \n 2. HISTORY \n 3. SPORTS \n 4. MUSIC \n 5. HUMAN-ANATOMY \n")
        val = val.strip()
        if val == "1" or val.lower() == "geography":
            playerGameOption = "GEOGRAPHY"
            num = 0
            break
        elif val == "2" or val.lower() == "history":
            playerGameOption = "HISTORY"
            num = 1
            break
        elif val == "3" or val.lower() == "sports":
            playerGameOption = "SPORTS"
            num = 2
            break
        elif val == "4" or val.lower() == "music":
            playerGameOption = "MUSIC"
            num = 3
            break
        elif val == "5" or val.lower() == "human-anatomy":
            playerGameOption = "HUMAN-ANATOMY"
            num = 4
            break
        else:
            print("\n Please select correct option \n")

    print("\n Get ready for the "+playerGameOption+" quiz\n")
    playerCount = 0
    playerCount = QuestionCategory(questionList, optionsList, questionAnswerList,
                                   playerQuestionReponseList, num, playerCount)

    Summary(questionList, playerQuestionReponseList, questionAnswerList, num)

    print("\x1b[0;30;43m""\nYour score is " +
          str(playerCount)+" out of 5"+"\x1b[0m")

    playerQuestionReponseList.clear()

    # Logic to play game again or to exit
    while True:
        playagain = input(
            "Do you want to play again?\n1. Yes\t2. No\nYou can also put the name (Case Insensitive)")
        # To remove the before and after spaces in the user supplied string
        playagain = playagain.strip()
        if playagain == "1" or playagain.lower() == "yes":
            break
        elif playagain == "2" or playagain.lower() == "no":
            quit()
        else:
            print("\nIncorrect option selected. Please select right option")
