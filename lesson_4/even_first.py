# Even First
# Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

# O(n)
def even_odd(arr: list):
     next_even = 0
     next_odd = len(arr) - 1
     while next_even < next_odd:
         if arr[next_even] % 2 == 0:
             next_even += 1
         else:
             arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
             next_odd -= 1
     return arr


test_list = [5, 3, 4, 6, 10, 9, 11]
print(test_list)
test_result_list = even_odd(test_list)
print(test_result_list)  # [4, 6, 10, ....]
print(test_list)