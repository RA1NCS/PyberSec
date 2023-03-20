# Author: Shreyan Gupta
# Date Started: 03/19/2023
# Date Completed: 03/19/2023

from random import randint


def HighestCommonFactor(number: int) -> int:
    for i in range(number - 1, 0, -1):
        if number % i == 0:
            return i
    return -1


def GeneratePrime(lowerlimit: int, upperlimit: int) -> int:
    while True:
        randomNumber = randint(lowerlimit, upperlimit)
        if HighestCommonFactor(randomNumber) == 1:
            return randomNumber


def CalculateE(r):
    while True:
        randomNumber = GeneratePrime(1, r)
        if HighestCommonFactor(randomNumber) == 1:
            return randomNumber


def RSA():
    p = GeneratePrime(0, 1000)
    q = GeneratePrime(0, 1000)

    n = p * q
    r = (p - 1) * (q - 1)
    e = CalculateE(r)

    while True:
        k = r * randint(0, 10) + 1
        d = HighestCommonFactor(k)
        if d == -1:
            print("INVALID D")
            exit(0)

        if d == 1:
            continue
        e = k // d
        if e != d:
            break

    return n, e, d


def EncryptMessage(message: str, e: int, n: int) -> str:
    newMessage = ""
    for letter in message:
        letter = ord(letter)
        newLetter = (letter**e) % n
        newMessage += str(newLetter) + " "
    return newMessage


def DecryptMessage(message: str, d: int, n: int) -> str:
    newMessage = ""
    messageArray = message.split()
    for number in messageArray:
        number = int(number)
        newNumber = (number**d) % n
        newLetter = chr(newNumber)
        newMessage += newLetter
    return newMessage


if __name__ == "__main__":
    encryptChoice = input("Do you want to encrypt or decrypt a message? (E/D)\n> ")

    if encryptChoice.lower() == "e":
        n, e, d = RSA()
        messageToEncrypt = input(
            "\nPlease enter the message you would like to encrypt here)\n> "
        )
        encryptedMessage = EncryptMessage(messageToEncrypt, e, n)
        print("\nEncrypted Message: " + encryptedMessage)
        print(f"\nGeneral Decyptor: {n}\nDecyption Key: {d}")

    elif encryptChoice.lower() == "d":
        print(
            "\nGuidelines:\n1. The message must be an RSA function applied to the ASCII values of a string\n2. The numbers must be separated by a space.\n"
        )

        messageToDecrypt = input(
            "\nPlease enter the message you would like to decrypt here)\n> "
        )
        n = int(input("\nPlease enter your general decryptor(n) here\n> "))
        d = int(input("\nPlease enter your decryption key (d) here\n> "))
        decryptedMessage = DecryptMessage(messageToDecrypt, d, n)
        print("\nDecrypted Message: " + decryptedMessage)

    else:
        print("Wrong choice, please re-run the program.")
