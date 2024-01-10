def convertIntToStr(integerNum):
    # create dict keys 0-9 with equivalent string value
    digit_to_char = {}
    for k, v in enumerate(range(10)):
        digit_to_char[k] = chr(48 + v)

    string_digits = ""
    negative = False

    # check for 0
    if integerNum == 0:
        return "0"

    # check for negative
    if integerNum < 0:
        integerNum = abs(integerNum)
        negative = True

    # create number string
    while integerNum != 0:
        working_digit = integerNum % 10
        string_digits = digit_to_char[working_digit] + string_digits
        integerNum = integerNum // 10

    # add negative if needed
    if negative:
        string_digits = "-" + string_digits

    return string_digits


def main():
    for i in range(-10000, 10000):
        assert convertIntToStr(i) == str(i)
    print(convertIntToStr(57))
    print(convertIntToStr(987057))
    print(convertIntToStr(-57))
    print(convertIntToStr(0))


if __name__ == "__main__":
    main()
