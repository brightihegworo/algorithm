
def sum_of_digits(number: int):
    result = 0
    for x in range(1, number + 1):
        result += x

    print(f'Put in {number} and got {result}')


test_num = 5

sum_of_digits(test_num)