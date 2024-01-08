def mode(numbers):
    if len(numbers) == 0:
        return None
    num_occur = {}
    most_frequent_num = numbers[0]
    for i in numbers:
        num_occur[i] = num_occur.get(i, 0) + 1
        if num_occur[i] > num_occur[most_frequent_num]:
            most_frequent_num = i
    return most_frequent_num


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
