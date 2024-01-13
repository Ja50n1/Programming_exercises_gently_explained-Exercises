def mergeTwoLists(list1, list2):
    result = []
    i1, i2 = 0, 0

    # add lesser index value to result and increment
    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] >= list2[i2]:
            result.append(list2[i2])
            i2 += 1
        elif list2[i2] > list1[i1]:
            result.append(list1[i1])
            i1 += 1

    # add remaing from longer list
    if i1 < len(list1):
        for item in list1[i1:]:
            result.append(item)
    elif i2 < len(list2):
        for item in list2[i2:]:
            result.append(item)
    return result


def main():
    assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]
    assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
    assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
    assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]
    assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]
    assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
    assert mergeTwoLists([], []) == []


if __name__ == "__main__":
    main()
