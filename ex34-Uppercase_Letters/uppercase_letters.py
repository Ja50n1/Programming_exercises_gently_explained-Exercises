def getUppercase(text):
    # create dictionary lowercase letters mapped to
    # their uppercase equivalent
    letter_dict = {}
    for lcase in range(97, 123):
        letter_dict[chr(lcase)] = chr(lcase - 32)

    # find any lowercase letters and convert to uppercase equivalent
    new_text = ""
    for character in text:
        if character in letter_dict:
            new_text = new_text + letter_dict[character]
        else:
            new_text = new_text + character

    return new_text


def main():
    assert getUppercase("Hello") == "HELLO"
    assert getUppercase("hello") == "HELLO"
    assert getUppercase("HELLO") == "HELLO"
    assert getUppercase("Hello, world!") == "HELLO, WORLD!"
    assert getUppercase("goodbye 123!") == "GOODBYE 123!"
    assert getUppercase("12345") == "12345"
    assert getUppercase("") == ""


if __name__ == "__main__":
    main()
