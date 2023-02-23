from secrets import randbelow


def randNum(lim) -> int:
    return randbelow(lim)


def randomCaesar():
    pass


if __name__ == "__main__":
    global i_passIn
    i_passIn = input("Enter the unhashed password here: ")
