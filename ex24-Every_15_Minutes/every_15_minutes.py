def main():
    for ampm in ("am", "pm"):
        for hour in (12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
            for quarter_hour in ("00", "15", "30", "45"):
                print(f"{hour}:{quarter_hour} {ampm}")


if __name__ == "__main__":
    main()
