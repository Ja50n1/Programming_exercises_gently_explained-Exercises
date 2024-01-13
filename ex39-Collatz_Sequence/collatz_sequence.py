import random


def collatz(startingNum):
    # Check for positive integer and non-zero
    if startingNum < 1:
        return []

    collatz_seq = [startingNum]
    n = startingNum
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_seq.append(n)
    return collatz_seq


def main():
    assert collatz(0) == []
    assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
    assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert len(collatz(256)) == 9
    assert len(collatz(257)) == 123

    random.seed(42)
    for i in range(1000):
        startingNum = random.randint(1, 10000)
        seq = collatz(startingNum)
        assert seq[0] == startingNum  # Make sure it includes the starting number.
        assert seq[-1] == 1  # Make sure the last integer is 1.


if __name__ == "__main__":
    main()
