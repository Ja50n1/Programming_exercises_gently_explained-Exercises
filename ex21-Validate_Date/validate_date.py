import datetime
import leap_year


def isValidDate(year, month, day):
    # check for valid month
    if 1 > month or month > 12:
        return False
    # check for leap year if feb 29
    if month == 2 and day == 29:
        if leap_year.isLeapYear(year):
            return True
        else:
            return False
    # check if day within month limits
    if (month == 2) and (day >= 1) and (day <= 28):
        return True
    elif (month in (4, 6, 9, 11)) and (day >= 1) and (day <= 30):
        return True
    elif (month in (1, 3, 5, 7, 8, 10, 12)) and (day >= 1) and (day <= 31):
        return True
    else:
        return False


def main():
    assert isValidDate(1999, 12, 31) == True
    assert isValidDate(2000, 2, 29) == True
    assert isValidDate(2001, 2, 29) == False
    assert isValidDate(2029, 13, 1) == False
    assert isValidDate(1000000, 1, 1) == True
    assert isValidDate(2015, 4, 31) == False
    assert isValidDate(1970, 5, 99) == False
    assert isValidDate(1981, 0, 3) == False
    assert isValidDate(1666, 4, 0) == False

    d = datetime.date(1970, 1, 1)
    oneDay = datetime.timedelta(days=1)
    for i in range(1000000):
        assert isValidDate(d.year, d.month, d.day) == True
        d += oneDay


if __name__ == "__main__":
    main()
