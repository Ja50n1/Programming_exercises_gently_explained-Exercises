def writeToFile(fname, text):
    # Open file in write mode
    with open(fname, "w") as fileObj:
        # write text to the file
        fileObj.write(text)


def appendToFile(fname, text):
    # Open file in append mode
    with open(fname, "a") as fileObj:
        # append text to the file
        fileObj.write(text)


def readFromFile(fname):
    # Open file in read mode
    with open(fname, "r") as fileObj:
        # read text from file and return as str
        return fileObj.read()


def main():
    writeToFile("greet.txt", "Hello!\n")
    appendToFile("greet.txt", "Goodbye!\n")
    assert readFromFile("greet.txt") == "Hello!\nGoodbye!\n"


if __name__ == "__main__":
    main()
