def reverseString(text):
    text_lst = list(text)
    newtext_lst = []

    for i in range((len(text_lst) - 1), -1, -1):
        newtext_lst.append(text_lst[i])

    return "".join(newtext_lst)


def main():
    assert reverseString("Hello") == "olleH"


assert reverseString("") == ""
assert reverseString("aaazzz") == "zzzaaa"
assert reverseString("xxxx") == "xxxx"

if __name__ == "__main__":
    main()
