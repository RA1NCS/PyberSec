# Author: Shreyan Gupta
# Date Started: 03/22/2023
# Date Completed: 03/24/2023

from secrets import randbelow
from inflect import engine
from string import punctuation
from word2number import w2n

inflectEngine = engine()

###############
### ENCRYPT ###
###############


def randomCaesar(i_passIn) -> str:
    m_randNum = randbelow(27)
    m_shifted = ""
    for char in i_passIn:
        mf_randNum = m_randNum
        m_isInt = False

        # Integer Validation
        try:
            int(char)
            m_isInt = True
        except ValueError:
            m_isInt = False

        # Letter Caesar Cipher
        if char.isalpha():
            m_caseCheck = 1 if char.isupper() else 2
            char = char.upper()
            m_charIndex = ord(char)
            if m_charIndex + mf_randNum > 90:
                m_charIndex -= 26
            m_upperChar = chr(m_charIndex + m_randNum).upper()
            m_newChar = m_upperChar if m_caseCheck == 1 else m_upperChar.lower()
            m_shifted += m_newChar

        # Number Reversing
        elif m_isInt:
            char = str(11 - int(char))
            m_shifted += char
        else:
            m_shifted += char
    return m_shifted, m_randNum


# Number to text
def numberToText(i_num: int) -> str:
    return inflectEngine.number_to_words(i_num)


# Return Random Punctuation
def randPunct() -> str:
    return punctuation[randbelow(31)]


# Removes all spaces and replaced them with a random character
def removeSpaces(i_origString: str) -> str:
    m_newString = ""
    for i in i_origString:
        if i == " ":
            i = randPunct()
        m_newString += i
    return m_newString


# Hexed Version
def stringToHex(i_passIn: str) -> str:
    # m_newText = ""
    m_keyOne = ""
    m_keyTwo = ""
    for letter in i_passIn:
        m_curIndex = hex(ord(letter))
        m_curIndex = m_curIndex[2:4]
        m_keyOne += m_curIndex[0:1]  # + "/"
        m_keyTwo += m_curIndex[1:2]  # + "/"
    return m_keyOne, m_keyTwo


# Remove Duplicates
def dupliRemove(i_origString: str) -> str:
    m_newString = ""
    m_repCount = 1
    for index, char in enumerate(i_origString):
        if index != (len(i_origString) - 1):
            if i_origString[index + 1] == char:
                m_repCount += 1
            else:
                m_newString += char + str(m_repCount) + randPunct()
                m_repCount = 1
        else:
            m_newString += char + str(m_repCount) + randPunct()

    return m_newString


###############
### DECRYPT ###
###############


# Converts hexadecimal keys back to string.
def HexToString(iKeyOne, iKeyTwo):
    mNewText = ""
    for i in range(len(iKeyOne)):
        mCharCode = int(iKeyOne[i] + iKeyTwo[i], 16)
        mNewText += chr(mCharCode)
    return mNewText


# Deciphers text encrypted with Caesar cipher using a given key.
def ReverseCaesar(iCipherText, iKey):
    mPlainText = ""
    for char in iCipherText:
        if char.isalpha():
            mCaseCheck = 1 if char.isupper() else 2
            char = char.upper()
            mCharIndex = ord(char)
            if mCharIndex - iKey < 65:
                mCharIndex += 26
            mUpperChar = chr(mCharIndex - iKey).upper()
            mNewChar = mUpperChar if mCaseCheck == 1 else mUpperChar.lower()
            mPlainText += mNewChar
        elif char.isdigit():
            mPlainText += str(11 - int(char))
        else:
            mPlainText += char
    return mPlainText


# Extracts and reconstructs the original string from the obfuscated string.
def GiveOriginalString(originalString):
    newString = ""
    for i in originalString:
        if (
            ord(i) < 48
            or ord(i) > 122
            or ord(i) in range(58, 63)
            or ord(i) in range(91, 96)
        ):
            newString += " "
        else:
            newString += i
    newString = newString.split("  ")
    iCipherText = newString[0]
    try:
        iKey = w2n.word_to_num(newString[-1])
        originalMessage = ReverseCaesar(iCipherText, iKey)
    except ValueError:
        originalMessage = "Error: Could not decrypt message."
    return originalMessage


# Removes punctuation from the input string and reconstructs the original characters.
def DeObfuscate(inputString):
    output = ""
    for char in inputString:
        if char in punctuation:
            inputString = inputString.replace(char, "")

    previousChar = inputString[0]
    for char in inputString:
        if char.isdigit():
            output += previousChar * int(char)
        else:
            previousChar = char
            if char.isalpha():
                output += char
    return output


#####################
### MAIN FUNCTION ###
#####################

if __name__ == "__main__":
    i_scriptMode = input(
        "Enter the script mode here (E | D):\nE. Encrypt\nD. Decrypt\n> "
    )

    if i_scriptMode == "E" or i_scriptMode == "e":
        i_passIn = input("Enter the unhashed password here: ")
        m_scrambledText, m_randShift = randomCaesar(i_passIn)
        m_stageTwoText = (
            m_scrambledText + randPunct() + randPunct() + numberToText(m_randShift)
        )
        m_stageThreeText = removeSpaces(m_stageTwoText)
        m_keyOne, m_keyTwo = stringToHex(m_stageThreeText)
        m_stageFiveTextA = dupliRemove(m_keyOne)
        m_stageFiveTextB = dupliRemove(m_keyTwo)

        print(f"Key 1 : {m_stageFiveTextA}")
        print(f"Key 2 : {m_stageFiveTextB}")

    elif i_scriptMode == "D" or i_scriptMode == "d":
        keyOne = input("Enter key 1 here: ")
        keyTwo = input("Enter key 2 here: ")
        keyOne = DeObfuscate(keyOne)
        keyTwo = DeObfuscate(keyTwo)
        originalString = HexToString(keyOne, keyTwo)
        actualString = GiveOriginalString(originalString)
        print(actualString)

    else:
        print(
            "Invalid Input. Please enter a valid mode (E | D), and re-run the script again."
        )
        exit()
