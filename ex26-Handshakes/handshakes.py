def printHandshakes(people):
    if len(people) < 2:
        return 0
    ctr = 0
    print(f"{people}")
    while len(people) > 1:
        person = people.pop()
        for i in people:
            print(f"{person} shakes hands with {i}")
            ctr += 1
    print(f"{ctr} handshkes in total.\n")
    return ctr


def main():
    assert printHandshakes(["Alice", "Bob"]) == 1
    assert printHandshakes(["Alice", "Bob", "Carol"]) == 3
    assert printHandshakes(["Alice", "Bob", "Carol", "David"]) == 6


if __name__ == "__main__":
    main()
