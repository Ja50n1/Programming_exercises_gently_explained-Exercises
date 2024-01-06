# import sys
# sys.path.insert(0, "/home/repos/gently_explained/ex13-Sum_and_Product")
from sum_and_product import calculateSum


def average(numbers):
    if len(numbers) == 0:
        return None
    sum_of_list_elements = calculateSum(numbers)
    return sum_of_list_elements / len(numbers)


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
