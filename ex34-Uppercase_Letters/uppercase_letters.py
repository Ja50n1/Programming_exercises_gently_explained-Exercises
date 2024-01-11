def getUppercase(text):
    pass


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
