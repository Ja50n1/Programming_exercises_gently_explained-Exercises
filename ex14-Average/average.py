from ../ex13-Sum_and_Product/sum_and_product import calculateSum



def average(numbers):
    if len(numbers) == 0:
        return None


def main():
    assert average([1, 2, 3]) == 2
    assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert average([12, 20, 37]) == 23
    assert average([0, 0, 0, 0, 0]) == 0
    import random

    random.seed(42)
    testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    for i in range(1000):
        random.shuffle(testData)
        assert average(testData) == 2


if __name__ == "__main__":
    main()
