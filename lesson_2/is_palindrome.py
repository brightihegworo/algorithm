
def is_palindrome(s):
    return s == s[::-1]
    # reverse_s = s[::-1]
    # if s == reverse_s:
    #     return True
    # else:
    #     return False

test_str_pos = "radar"
test_str_neg = "radax"
result_pos = is_palindrome(test_str_pos)

print(result_pos)