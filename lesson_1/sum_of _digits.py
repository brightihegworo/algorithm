#0(n)
# def sum_of_digits(number: int):
#     result = 0
#     for x in range(1, number + 1):
#         result += x
#
#     print(f'Put in {number} and got {result}')

#0(1)
def sum_of_digits(number: int):
    final_sum = (number * (number + 1)) / 2
    return final_sum


test_num = 7

result = sum_of_digits(test_num)

print(result)