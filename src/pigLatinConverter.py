import re


# Function to handle other characters
def handleSpecialCharacters(str):
    str1 = ""
    str2 = ""
    str3 = ""
    if re.match("[^0-9a-zA-Z]", str[len(str)-1]) and re.match("[^0-9a-zA-Z]", str[0]):
        str1 = str[1:len(str)-1]
        str2 = str[len(str)-1]
        str3 = str[0]
    elif re.match("[^0-9a-zA-Z]", str[0]):
        str1 = str[1:len(str)]
        str3 = str[0]
    elif re.match("[^0-9a-zA-Z]", str[len(str)-1]):
        str1 = str[0:len(str)-1]
        str2 = str[len(str)-1]
    else:
        str1 = str
    return str1, str2, str3


statementToConvert = input(
    "Enter a text or statement to convert. If you are entering a compound text, please enter space between them. Example - Bathroom -> Bath room : ")
statementToConvert = statementToConvert.strip()
textList = statementToConvert.split()
pigLatinStatement = ""


for textToConvert in textList:
    pigLatinText = ""
    lenofString = len(textToConvert)
    list1 = handleSpecialCharacters(textToConvert)
    textToConvert = list1[0]

    # Word beginning with consonant
    if re.match("[^aeiouAEIOU][aeiouAEIOU]\s*", textToConvert):
        pigLatinText = list1[2]+textToConvert[1:lenofString] + \
            textToConvert[0] + "ay"+list1[1]
        pigLatinStatement = pigLatinStatement+" "+pigLatinText

    # Word begining with consonant clusters or including y after consonant cluster
    elif re.match("[^aeiouyAEIOUY]{2,}\s*", textToConvert):
        i = 0
        for val in textToConvert:
            if val.lower() not in ["a", "e", "i", "o", "u", "y"]:
                i += 1
            else:
                break
        pigLatinText = list1[2]+textToConvert[i:lenofString] + \
            textToConvert[0:i]+"ay"+list1[1]
        pigLatinStatement = pigLatinStatement+" "+pigLatinText

    # Word beginning with vowel or y
    elif re.match("^[aeiouyAEIOUY]\s*", textToConvert):
        pigLatinText = list1[2]+textToConvert+"yay"+list1[1]
        pigLatinStatement = pigLatinStatement+" "+pigLatinText

    # Word having y as second character
    elif re.match("[^yY][yY]\s*", textToConvert):
        pigLatinText = list1[2]+textToConvert[1:len(
            textToConvert)]+textToConvert[0]+"ay"+list1[1]
        pigLatinStatement = pigLatinStatement+" "+pigLatinText
        print(pigLatinText)
    else:
        pigLatinStatement = pigLatinStatement+" "+textToConvert

print(pigLatinStatement.strip())
