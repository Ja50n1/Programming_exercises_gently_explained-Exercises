def plural(bottle_count):
    if bottle_count == 1:
        return ""
    else:
        return "s"


def main():
    for count in range(100, 0, -1):
        print(f"{count} bottle{plural(count)} of beer on the wall,")
        print(f"{count} bottle{plural(count)} of beer,")
        print("Take one down,")
        print("Pass it around,")
        if count > 1:
            print(f"{count - 1} bottle{plural(count - 1)} of beer on the wall.\n")
        else:
            print(f"No more bottles of beer on the wall!")


if __name__ == "__main__":
    main()
