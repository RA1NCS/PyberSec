# Author: Shreyan Gupta
# Date Started: 02/09/2023
# Date Completed: 02/11/2023


def caesarCipher(i_passIn: str, i_shiftIn: int) -> str:
    m_shifted = ""
    for char in i_passIn:
        mf_randNum = i_shiftIn
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
            m_upperChar = chr(m_charIndex + i_shiftIn).upper()
            m_newChar = m_upperChar if m_caseCheck == 1 else m_upperChar.lower()
            m_shifted += m_newChar

        # Number Reversing
        elif m_isInt:
            char = str(11 - int(char))
            m_shifted += char
        else:
            m_shifted += char
    return m_shifted


def reverseCaesar(i_cipherText, i_key):
    m_plaintext = ""
    for char in i_cipherText:
        if char.isalpha():
            m_caseCheck = 1 if char.isupper() else 2
            char = char.upper()
            m_charIndex = ord(char)
            if m_charIndex - i_key < 65:
                m_charIndex += 26
            m_upperChar = chr(m_charIndex - i_key).upper()
            m_newChar = m_upperChar if m_caseCheck == 1 else m_upperChar.lower()
            m_plaintext += m_newChar
        elif char.isdigit():
            m_plaintext += str(11 - int(char))
        else:
            m_plaintext += char
    return m_plaintext


if __name__ == "__main__":
    i_checkCrypt = input("Do you wish to decrypt or encrypt your text?\n> ")

    if i_checkCrypt.lower() == "decrypt":
        i_messageIn = input("\nPlease enter your message here:\n> ")
        i_shiftIn = input("\nPlease enter the shift you wish for:\n> ")
        print(
            f"\nThe decrypted message is: {reverseCaesar(i_messageIn, int(i_shiftIn))}"
        )

    elif i_checkCrypt.lower() == "encrypt":
        i_messageIn = input("\nPlease enter your message here:\n> ")
        i_shiftIn = input("\nPlease enter the shift you wish for:\n> ")
        print(
            f"\nThe encrypted message is: {caesarCipher(i_messageIn, int(i_shiftIn))}"
        )
    else:
        print("\nWrong input entered, please run the program again.")
