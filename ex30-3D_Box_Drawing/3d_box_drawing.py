"""
Sample drawBox(5)
      +----------+
     /          /|
    /          / |
   /          /  |
  /          /   |
 /          /    |
+----------+     +
|          |    /
|          |   /
|          |  /
|          | /
|          |/
+----------+
"""


def drawBox(size):
    # check for minimum size
    if size < 1:
        return ""

    # print top and top side of side
    print(" " * (size + 1) + "+" + "--" * size + "+")
    for forward, reverse in enumerate(range(size, 0, -1)):
        print(" " * reverse, end="")
        print("/" + "  " * size + "/", end="")
        print(" " * forward + "|")
    print("+" + "--" * size + "+" + " " * size + "+")

    # print front and bottom side of side
    for forward, reverse in enumerate(range((size - 1), -1, -1)):
        print("|" + "  " * size + "|" + " " * reverse + "/")
    print("+" + "--" * size + "+")


def main():
    drawBox(5)
    drawBox(4)
    drawBox(3)
    drawBox(2)
    drawBox(1)
    drawBox(0)


if __name__ == "__main__":
    main()
