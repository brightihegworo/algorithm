
def below_arithmetical_mean(arr):
    arithmetical_mean = sum(arr) / len(arr)
    print(f"Arithmetical mean: {arithmetical_mean}")
    final_list =[]
    for element in arr:
        if element < arithmetical_mean:
            final_list.append(element)
    return final_list


test_list = [1, 3, 5, 6, 4, 10, 2, 3]
test_result = below_arithmetical_mean(test_list)
print(test_result)