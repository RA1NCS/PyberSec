from secrets import randbelow
from inflect import engine
from string import punctuation

inflectEngine = engine()


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


# ASCII Version
# def stringToHex(i_passIn: str) -> str:
#     m_newText = ""
#     for letter in i_passIn:
#         m_curIndex = str(ord(letter))
#         if len(m_curIndex) == 2:
#             m_curIndex = "0" + m_curIndex
#         m_newText += m_curIndex + randPunct()
#     return m_newText


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


# Main Function
if __name__ == "__main__":
    i_passIn = input("Enter the unhashed password here: ")
    m_scrambledText, m_randShift = randomCaesar(i_passIn)
    m_stageTwoText = (
        m_scrambledText + randPunct() + randPunct() + numberToText(m_randShift)
    )
    m_stageThreeText = removeSpaces(m_stageTwoText)
    m_keyOne, m_keyTwo = stringToHex(m_stageThreeText)
    m_stageFiveTextA = dupliRemove(m_keyOne)
    m_stageFiveTextB = dupliRemove(m_keyTwo)

    print(m_keyOne, m_stageFiveTextA)
    print(m_keyTwo, m_stageFiveTextB)
