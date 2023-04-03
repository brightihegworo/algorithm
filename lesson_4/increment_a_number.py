# Write a program that takes as input an array of digits encoding a nonnegative decimal integer D
# and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
# O(n)
def plus_one(arr: list):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

test_digit1 = [1, 2, 3]  # => 1, 2, 4
test_digit2 = [1, 9, 9]  # => 2, 0, 0
test_digit3 = [9, 9, 9]  # => 1, 0, 0, 0
print(plus_one(test_digit1))
print(plus_one(test_digit2))
print(plus_one(test_digit3))