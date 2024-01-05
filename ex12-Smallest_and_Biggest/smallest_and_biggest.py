def getSmallest(numbers):
    if len(numbers) == 0:
        return None
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest


def getBiggest(numbers):
    if len(numbers) == 0:
        return None
    biggest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > biggest:
            biggest = numbers[i]
    return biggest


def main():
    assert getSmallest([1, 2, 3]) == 1
    assert getSmallest([3, 2, 1]) == 1
    assert getSmallest([28, 25, 42, 2, 28]) == 2
    assert getSmallest([1]) == 1
    assert getSmallest([]) == None
    assert getBiggest([]) == None
    assert getBiggest([1, 2, 3]) == 3
    assert getBiggest([3, 2, 1]) == 3
    assert getBiggest([28, 25, 42, 2, 28]) == 42
    assert getBiggest([3]) == 3


if __name__ == "__main__":
    main()
