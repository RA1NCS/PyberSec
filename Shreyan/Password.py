# Author: Shreyan Gupta
# Date Started: 02/09/2023
# Date Completed: 02/09/2023

import random


def passGen(i_length):
    s_lowerLetters = "abcdefghijklmnopqrstuvwxyz"
    s_upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s_numbers = "0123456789"
    s_characters = "!()-.?[]_`~;:!@#$%^&*+="

    l_randomList = [s_lowerLetters, s_upperLetters, s_numbers, s_characters]
    finalString = ""
    for i in range(0, i_length):
        m_randomList = random.randint(0, 3)
        m_chosenList = l_randomList[m_randomList]
        m_chosenLen = len(m_chosenList)
        m_chooseChar = random.randint(0, m_chosenLen - 1)
        m_charChosen = m_chosenList[m_chooseChar]
        finalString += m_charChosen

    return finalString


if __name__ == "__main__":
    i_passCount = int(
        input("Please enter the number of passwords you wish to create: ")
    )
    i_passLength = int(
        input("Please enter the length of each password in characters: ")
    )
    print()
    for i in range(0, i_passCount):
        print(f"Password {i + 1}: {passGen(i_passLength)}")
