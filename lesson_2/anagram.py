def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    elif sorted(s1) == sorted(s2):
        return True
    else:
        return False

test_str_1 = "abcd"
test_str_2 = "cadb"

result = is_anagram(test_str_1, test_str_2)

print(result)
