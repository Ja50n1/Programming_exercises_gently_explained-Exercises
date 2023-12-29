def fizzBuzz(upTo):
    if upTo < 1 or type(upTo) != int:
        print("Number must be integer greater zero")
        return
    i = 1
    while i <= upTo:
        if i % 15 == 0:
            print("FizzBuzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        else:
            print(i, " ", end="")
        i += 1
    print()


fizzBuzz(35)
