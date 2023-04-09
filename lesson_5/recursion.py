
def recursion(number: int):
    if number == 0:
        return
    print(number)
    number -= 1
    recursion(number)


recursion(10)