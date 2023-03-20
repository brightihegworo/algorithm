# Given a string. Split it into two equal parts.
# Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.

# O(1)

def split_in_half(s):
     length = len(s)
     half = length // 2
     add = 0
     if length % 2:
         add = 1
     left = s[:half + add]
     right = s[half + add:]
     return right + left


test_even = "aaabbb"  # bbbaaa
test_odd = "aaabbbb"  # bbbaaab
result_even = split_in_half(test_even)
print(result_even)
result_odd = split_in_half(test_odd)
print(result_odd)