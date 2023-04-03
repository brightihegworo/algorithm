
#O(n)

def find_max_element(arr):
    max_index = 0
    max_num = arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i

    print(f"Max number: {max_num}")
    print(f"Max index: {max_index}")

test_list = [5, 32, 5, 4, 16, 17, 3]
find_max_element(test_list)

