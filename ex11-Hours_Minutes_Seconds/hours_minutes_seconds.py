def getHoursMinutesSeconds(totalSeconds):
    hrs, mins, secs = "", "", ""
    if totalSeconds // 3600 > 0:
        hrs = str(totalSeconds // 3600) + "h"
        totalSeconds -= totalSeconds // 3600 * 3600
    if totalSeconds // 60 > 0:
        mins = " " + str(totalSeconds // 60) + "m"
        totalSeconds -= totalSeconds // 60 * 60
    if totalSeconds > 0:
        secs = " " + str(totalSeconds) + "s"
    elif totalSeconds == 0 and (hrs == "" and mins == ""):
        secs = "0s"
    return (hrs + mins + secs).strip()


def getDaysHoursMinutesSeconds(totalSeconds):
    days = ""
    d = 60 * 60 * 24
    if totalSeconds // d > 0:
        days = str(totalSeconds // d) + "d "
        totalSeconds -= totalSeconds // d * d
        return (days + getHoursMinutesSeconds(totalSeconds)).strip()
    else:
        return getHoursMinutesSeconds(totalSeconds)


def main():
    assert getHoursMinutesSeconds(30) == "30s"
    assert getHoursMinutesSeconds(60) == "1m"
    assert getHoursMinutesSeconds(90) == "1m 30s"
    assert getHoursMinutesSeconds(3600) == "1h"
    assert getHoursMinutesSeconds(3601) == "1h 1s"
    assert getHoursMinutesSeconds(3661) == "1h 1m 1s"
    assert getHoursMinutesSeconds(90042) == "25h 42s"
    assert getHoursMinutesSeconds(0) == "0s"
    assert getDaysHoursMinutesSeconds(90042) == "1d 1h 42s"
    assert getDaysHoursMinutesSeconds(3661) == "1h 1m 1s"


if __name__ == "__main__":
    main()
