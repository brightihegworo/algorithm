


def count_odd_and_even_numbers(number: int):
    even_num = 0
    odd_num = 0
    number = str(number)
    for x in number:
        x = int(x)
        if x % 2 == 0:
            even_num += 1
        else:
            odd_num += 1

    print(f'Even Count: {even_num} and Odd Count: {odd_num}')



test_num = 24689334
count_odd_and_even_numbers(test_num)