def getChessSquareColor(column, row):
    # check for type int
    if type(column) != int or type(row) != int:
        return ""
    # check column, row are within range 0-7
    if (7 >= column >= 0) == False or (7 >= row >= 0) == False:
        return ""
    if column % 2 == row % 2:
        return "white"
    else:
        return "black"


def main():
    assert getChessSquareColor(0, 0) == "white"
    assert getChessSquareColor(1, 0) == "black"
    assert getChessSquareColor(0, 1) == "black"
    assert getChessSquareColor(7, 7) == "white"
    assert getChessSquareColor(0, 8) == ""
    assert getChessSquareColor(2, 9) == ""


if __name__ == "__main__":
    main()
