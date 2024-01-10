def drawPyramid(height):
    spaces = height - 1
    for h in range(1, height + 1):
        print(" " * spaces + "#" + "#" * ((h - 1) * 2))
        spaces -= 1


def main():
    drawPyramid(6)
    drawPyramid(0)
    drawPyramid(-1)
    drawPyramid(5)


if __name__ == "__main__":
    main()
