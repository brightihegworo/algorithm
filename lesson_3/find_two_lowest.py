
def find_two_lowest(arr):
    arr.sort()
    return arr[:2]


test_list = [54, 32, 1, 43, 9, 16]
test_result = find_two_lowest(test_list)
print(test_result)