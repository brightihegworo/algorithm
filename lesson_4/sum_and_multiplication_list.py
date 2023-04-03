def print_sum_and_mult(arr):
    sum_of_list = 0
    mult_of_list = 1
    for e in arr:
        sum_of_list += e
        mult_of_list *= e

    print(f"The orginal list: {arr}")
    print(f"Sum of all elements: {sum_of_list}")
    print(f"Multiplication of all elements: {mult_of_list}")

test_list = [1,7, 3]

print_sum_and_mult(test_list)