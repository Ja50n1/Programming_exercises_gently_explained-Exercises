def bubbleSort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    print(numbers)
    return numbers


def main():
    assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
    assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]


if __name__ == "__main__":
    main()
