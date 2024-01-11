def commaFormat(number):
    # convert int number to string
    num_str = str(number)

    # check for float and slice decimal portion from integer portion
    decimal = ""
    if "." in num_str and num_str.index(".") > 3:
        decimal = num_str[num_str.index(".") :]
        num_str = num_str[: num_str.index(".")]

    # add commas to num, if neccessary
    new_num_str = ""
    num_str_lst = list(num_str)

    if len(num_str) > 3:
        for _ in range(len(num_str) // 3):
            for _ in range(3):
                digit = num_str_lst.pop()
                new_num_str = digit + new_num_str
            if num_str_lst == []:
                new_num_str = new_num_str
            else:
                new_num_str = "," + new_num_str
    return "".join(num_str_lst) + new_num_str + decimal


def main():
    assert commaFormat(1) == "1"
    assert commaFormat(10) == "10"
    assert commaFormat(100) == "100"
    assert commaFormat(1000) == "1,000"
    assert commaFormat(10000) == "10,000"
    assert commaFormat(100000) == "100,000"
    assert commaFormat(1000000) == "1,000,000"
    assert commaFormat(1234567890) == "1,234,567,890"
    assert commaFormat(1000.123456) == "1,000.123456"


if __name__ == "__main__":
    main()
