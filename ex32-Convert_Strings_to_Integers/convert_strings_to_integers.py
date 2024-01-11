def convertStrToInt(stringNum):
    str_to_int = {}
    for v, k in enumerate(range(10)):
        str_to_int[chr(48 + k)] = v

    # check for negative
    negative = False
    if stringNum[0] == "-":
        stringNum = stringNum[1:]
        negative = True

    # convert string to int
    num = 0
    for i in list(stringNum):
        num = num * 10 + str_to_int[i]

    if negative:
        num = num * -1

    return num


def main():
    for i in range(-10000, 10000):
        assert convertStrToInt(str(i)) == i
    # assert (convertStrToInt("421")) == 421
    # print(convertStrToInt("421"))
    # print(type(convertStrToInt("421")))


if __name__ == "__main__":
    main()
