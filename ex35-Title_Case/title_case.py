def getTitleCase(text):
    text_lst = list(text)
    titledText = ""
    for i, char in enumerate(text_lst):
        if i == 0:
            titledText = titledText + char.upper()
        elif char.isalpha() and text_lst[i - 1].isalpha():
            titledText = titledText + char.lower()
        else:
            titledText = titledText + char.upper()
    return titledText


def main():
    assert getTitleCase("Hello, world!") == "Hello, World!"
    assert getTitleCase("HELLO") == "Hello"
    assert getTitleCase("hello") == "Hello"
    assert getTitleCase("hElLo") == "Hello"
    assert getTitleCase("") == ""
    assert getTitleCase("abc123xyz") == "Abc123Xyz"
    assert getTitleCase("cat dog RAT") == "Cat Dog Rat"
    assert getTitleCase("cat,dog,RAT") == "Cat,Dog,Rat"

    import random

    random.seed(42)
    chars = list("abcdefghijklmnopqrstuvwxyz1234567890 ,.")
    for i in range(1000):
        random.shuffle(chars)
        assert getTitleCase("".join(chars)) == "".join(chars).title()


if __name__ == "__main__":
    main()
