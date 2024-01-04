# The Easy Way ...
# def findAndReplace(text, oldText, newText):
#     return text.replace(oldText, newText)


# The hard way ...
def findAndReplace(text, oldText, newText):
    i = 0
    replaced_text = ""
    while i < len(text):
        if oldText == text[i : i + len(oldText)]:
            i += len(oldText)
            replaced_text = replaced_text + newText
        else:
            replaced_text = replaced_text + text[i]
            i += 1
    return replaced_text


def main():
    assert findAndReplace("The fox", "fox", "dog") == "The dog"
    assert findAndReplace("fox", "fox", "dog") == "dog"
    assert findAndReplace("Firefox", "fox", "dog") == "Firedog"
    assert findAndReplace("foxfox", "fox", "dog") == "dogdog"
    assert findAndReplace("The Fox and fox.", "fox", "dog") == "The Fox and dog."


if __name__ == "__main__":
    main()
