# Using for loop
def list_without_duplicate_1(input_list):
    output = []
    for element in input_list:
        if element not in output:
            output.append(element)
    return output


# Using set
def list_without_duplicate_2(input_list):
    output = set()
    for element in input_list:
        output.add(element)
    return list(output)


test_case = [1, 1, 2, 3, 4, 2, 6, 7, 7]

print(list_without_duplicate_1(test_case))
print(list_without_duplicate_2(test_case))

