def longest_consecutive_subsequence(input_list):
    # iterate over the list and store element in a suitable data structure
    element_dict = dict()

    for index, element in enumerate(input_list):
        element_dict[element] = index

    # traverse / go over the data structure in a reasonable order to determine the solution
    max_length = -1
    starts_at = len(input_list)

    for index, element in enumerate(input_list):
        current_index = index
        element_dict[element] = -1

        current_count = 1

        # check upwards
        current_element = element + 1

        while current_element in element_dict and element_dict[current_element] > 0:
            current_count += 1
            element_dict[current_element] = -1
            current_element = current_element + 1

        # check downwards
        current_element = element - 1
        while current_element in element_dict and element_dict[current_element] > 0:
            current_index = element_dict[current_element]
            current_count += 1
            element_dict[current_element] = -1
            current_element = current_element - 1

        if current_count >= max_length:
            if current_count == max_length and current_index > starts_at:
                continue
            starts_at = current_index
            max_length = current_count

    start_element = input_list[starts_at]
    return [element for element in range(start_element, start_element + max_length)]


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


# Test case 1
test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)

# Test case 2
test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6], [8, 9, 10, 11, 12]]
test_function(test_case_2)

# Test case 3
test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)