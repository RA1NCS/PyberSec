from word2number import w2n
import string


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
    iKey = w2n.word_to_num(newString[-1])
    originalMessage = ReverseCaesar(iCipherText, iKey)
    return originalMessage


# Removes punctuation from the input string and reconstructs the original characters.
def DeObfuscate(inputString):
    output = ""
    for char in inputString:
        if char in string.punctuation:
            inputString = inputString.replace(char, "")

    print(inputString)
    previousChar = inputString[0]
    for char in inputString:
        if char.isdigit():
            output += previousChar * int(char)
        else:
            previousChar = char
            if char.isalpha():
                output += char
    return output


if __name__ == "__main__":
    keyOne = "71%61^73#61+72`32*21/31%64@71("  # input("Enter key 1 here: ")
    keyTwo = (
        "01|d1^42-71_a2?71%81.21<51?f1!51#91|71<81.41-"  # input("Enter key 2 here: ")
    )

    keyOne = DeObfuscate(keyOne)
    keyTwo = DeObfuscate(keyTwo)
    print(keyOne, keyTwo)
    originalString = HexToString(keyOne, keyTwo)
    actualString = GiveOriginalString(originalString)
    print(actualString)
