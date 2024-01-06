def median(numbers):
    if len(numbers) == 0:
        return None
    srtd_nums = sorted(numbers)
    if len(numbers) % 2 == 0:
        high_middle_index = len(numbers) // 2
        return (srtd_nums[high_middle_index] + srtd_nums[high_middle_index - 1]) / 2
    else:
        return srtd_nums[len(numbers) // 2]


def main():
    assert median([]) == None
    assert median([1, 2, 3]) == 2
    assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
    assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
    import random

    random.seed(42)
    testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
    for i in range(1000):
        random.shuffle(testData)
        assert median(testData) == 6


if __name__ == "__main__":
    main()
