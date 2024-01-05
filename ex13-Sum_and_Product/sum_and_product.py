def calculateSum(numbers):
    if len(numbers) == 0:
        return 0
    sum_tot = 0
    for i in range(len(numbers)):
        sum_tot += numbers[i]
    return sum_tot


def calculateProduct(numbers):
    if len(numbers) == 0:
        return 1
    product_tot = 1
    for i in range(len(numbers)):
        product_tot *= numbers[i]
    return product_tot


def main():
    assert calculateSum([]) == 0
    assert calculateSum([2, 4, 6, 8, 10]) == 30
    assert calculateProduct([]) == 1
    assert calculateProduct([2, 4, 6, 8, 10]) == 3840
    assert calculateSum([2, 4, 6, 8.6, 10]) == 30.6


if __name__ == "__main__":
    main()
