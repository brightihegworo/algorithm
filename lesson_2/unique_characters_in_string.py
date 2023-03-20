# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return false.

def uni_char(s):
     chars = set()

     for char in s:
         if char in chars:
             return False
         else:
             chars.add(char)
             print(char)

     return True

#def uni_char(s):
    #return len(set(s)) == len(s)

test_pos = "abcde"
test_neg = "abcdb"

set_test_pos = set(test_pos)
set_test_neg = set(test_neg)
print(" pos string ")
print(test_pos)
print(" pos set")
print(set_test_pos)

print("\n\n neg string ")
print(test_neg)
print(" neg set")
print(set_test_neg)

result_pos = uni_char(test_pos)
print(result_pos)  # True
result_neg = uni_char(test_neg)
print(result_neg)  # False