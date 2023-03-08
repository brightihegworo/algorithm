
#O(1)
def swap_variables(a:int, b:int):
    print(f"Before swap: a = {a}, b = {b}") # a = 5, b = 10
    temp = a
    a = b
    b = temp
    print(f"Before swap: a = {a}, b = {b}") # a = 10, b = 5



test_a = 5
test_b = 10

swap_variables(test_a, test_b)


# same thing O(1)
def swap_variables(a:int, b:int):
    print(f"Before swap: a = {a}, b = {b}") # a = 5, b = 10
    a = a + b
    b = a - b
    a = a - b
    print(f"Before swap: a = {a}, b = {b}") # a = 10, b = 5



test_a = 5
test_b = 10

swap_variables(test_a, test_b)


# same thing O(1)
def swap_variables(a:int, b:int):
    print(f"Before swap: a = {a}, b = {b}") # a = 5, b = 10
    a, b = b, a
    print(f"Before swap: a = {a}, b = {b}") # a = 10, b = 5



test_a = 5
test_b = 10

swap_variables(test_a, test_b)