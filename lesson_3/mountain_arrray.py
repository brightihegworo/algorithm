
def is_mountain(arr):
    i = 1

    while i < len(arr) and arr[i - 1] < arr[i]:
        i += 1
    if i == 1 or i == len(arr):
        return False

    while i < len(arr) and arr[i - 1] > arr[i]:
        i += 1

    if i == len(arr):
        return True

    return False

test_pos = [1, 3, 6, 7, 5]
test_neg = [1, 2, 4, 2, 3, 1]
result_pos = is_mountain(test_pos)
print(result_pos)
result_neg = is_mountain(test_neg)
print(result_neg)