def mode(numbers):
    pass


def main():
    assert mode([]) == None
    assert mode([1, 2, 3, 4, 4]) == 4
    assert mode([1, 1, 2, 3, 4]) == 1
    import random

    random.seed(42)
    testData = [1, 2, 3, 4, 4]
    for i in range(1000):
        random.shuffle(testData)
        assert mode(testData) == 4


if __name__ == "__main__":
    main()
