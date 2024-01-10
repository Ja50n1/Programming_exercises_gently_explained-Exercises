def drawBorder(width, height):
    if width < 2 or height < 2:
        return ""
    for h in range(height):
        if h == 0 or h == (height - 1):
            print("+" + " -" * (width - 3) + " +")
        else:
            print("|" + "  " * (width - 3) + " |")


def main():
    drawBorder(16, 4)
    drawBorder(5, 4)
    drawBorder(2, 2)


if __name__ == "__main__":
    main()
