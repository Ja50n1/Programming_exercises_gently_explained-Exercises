def mlutiplication_table(factor):
    # header
    print(f"{'  |'}", end="")
    for i in range(1, factor + 1):
        print(f"{i:>3} ", end="")
        if i == (factor):
            print("")

    # horizontal separator
    print(f"{'--+'}", end="")
    for i in range(1, factor + 1):
        print(f"----", end="")
        if i == (factor):
            print("")

    # print table rows
    for row in range(1, factor + 1):
        print(f"{row:>2}|", end="")
        for column in range(1, factor + 1):
            print(f"{column * row:>3} ", end="")
            if column == (factor):
                print("")


def main():
    mlutiplication_table(10)


if __name__ == "__main__":
    main()
