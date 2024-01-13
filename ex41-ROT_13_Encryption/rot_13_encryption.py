def rot13(text):
    rot13_str = ""
    for char in text:
        if char.isalpha():
            if 122 >= ord(char) >= 97:
                if (ord(char) + 13) > 122:
                    e_char = chr(ord(char) - 13)
                else:
                    e_char = chr(ord(char) + 13)
            else:
                if (ord(char) + 13) > 90:
                    e_char = chr(ord(char) - 13)
                else:
                    e_char = chr(ord(char) + 13)
            rot13_str = rot13_str + e_char
        else:
            rot13_str = rot13_str + char
    return rot13_str


def main():
    assert rot13("Hello, world!") == "Uryyb, jbeyq!"
    assert rot13("Uryyb, jbeyq!") == "Hello, world!"
    assert rot13(rot13("Hello, world!")) == "Hello, world!"
    assert rot13("abcdefghijklmnopqrstuvwxyz") == "nopqrstuvwxyzabcdefghijklm"
    assert rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "NOPQRSTUVWXYZABCDEFGHIJKLM"


if __name__ == "__main__":
    main()
