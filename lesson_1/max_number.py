
def max_number(num_1: int, num_2: int, num_3: int):
    if num_1 > num_2 and num_1 > num_3:
        print(f'Max number is {num_1}')
    elif num_2 > num_1 and num_2 > num_3:
        print(f'Max number is {num_2}')
    else:
        print(f'Max number is {num_3}')



test_1 = 89
test_2 = 73
test_3 = 9


max_number(test_1, test_2, test_3)