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
    n, e, d = RSA()
    print(f"n: {n} | e: {e} | d: {d}")
    messageToInput = input("Please enter the message you would like to encrypt here: ")
    encryptedMessage = EncryptMessage(messageToInput, e, n)
    decryptedMessage = DecryptMessage(encryptedMessage, d, n)
    print(encryptedMessage)
    print(decryptedMessage)
