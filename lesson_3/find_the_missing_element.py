def find_missing_number(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for i in range(len(arr2) - 1):
        if arr1[i] != arr2[i]:
            return arr1[i]

    return arr1[-1]


test_arr1 = [2, 3, 1, 4]
test_arr2 = [4, 1, 3]
result = find_missing_number(test_arr1, test_arr2)

print(result)