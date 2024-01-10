def drawRectangle(width, height):
    if width < 1 or height < 1:
        return ""
    for _ in range(height):
        for _ in range(width):
            print("#", end="")
        print()


def main():
    drawRectangle(16, 4)


if __name__ == "__main__":
    main()
