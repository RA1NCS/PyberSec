# Author: Shreyan Gupta
# Date Started: 02/09/2023
# Date Completed:
# Quite lousy script for a ROT13 cipher, made in about 15 minutes.


def encrypt(message, shift):
    s_wordList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    m_newWord = ""
    for i in message:
        m_curLetter = i
        m_curIndex = s_wordList.find(m_curLetter)

        m_newIndex = m_curIndex + shift
        if m_newIndex > 52:
            m_newIndex = m_newIndex % 52
        m_newChar = s_wordList[m_newIndex]
        m_newWord += m_newChar

    if message.islower():
        return m_newWord.lower()
    elif message.isupper():
        return m_newWord.upper()


if __name__ == "__main__":
    i_messageIn = input("Please enter your message here: ")
    i_shiftIn = input("Please enter the shift you wish for: ")

    print(encrypt(i_messageIn, int(i_shiftIn)))
