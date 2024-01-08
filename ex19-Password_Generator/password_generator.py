from random import randint, shuffle

# define constants
LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SPECIAL = "~!@#$%^&*()_+"


def generatePassword(length):
    if length < 12:
        length = 12
    combined_string = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
    password = []
    password.append(LOWER_LETTERS[randint(0, 25)])
    password.append(UPPER_LETTERS[randint(0, 25)])
    password.append(NUMBERS[randint(0, 9)])
    password.append(SPECIAL[randint(0, 12)])
    while len(password) < length:
        password.append(combined_string[randint(0, 74)])
    shuffle(password)
    password_str = "".join(password)
    print(password_str)
    return password_str


def main():
    assert len(generatePassword(8)) == 12
    pw = generatePassword(14)
    assert len(pw) == 14
    hasLowercase = False
    hasUppercase = False
    hasNumber = False
    hasSpecial = False
    for character in pw:
        if character in LOWER_LETTERS:
            hasLowercase = True
        if character in UPPER_LETTERS:
            hasUppercase = True
        if character in NUMBERS:
            hasNumber = True
        if character in SPECIAL:
            hasSpecial = True
    assert hasLowercase and hasUppercase and hasNumber and hasSpecial


if __name__ == "__main__":
    main()
