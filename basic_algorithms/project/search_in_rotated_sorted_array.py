def rotated_array_search(input_list, start_index, end_index, target_number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(list): Input list to search
       target_number(int): the target number
    Returns:
       int: Index or -1
    """

    if start_index > end_index:
        return -1

    middle_index = (start_index + end_index) // 2
    middle_value = input_list[middle_index]

    if middle_value == target_number:
        return middle_index

    elif input_list[start_index] <= middle_value:
        if input_list[start_index] <= target_number <= middle_value:
            return rotated_array_search(input_list, start_index, middle_index - 1, target_number)
        return rotated_array_search(input_list, middle_index + 1, end_index, target_number)

    else:
        if middle_value <= target_number <= input_list[end_index]:
            return rotated_array_search(input_list, middle_index + 1, end_index, target_number)
        return rotated_array_search(input_list, start_index, middle_index - 1, target_number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    start_index = 0
    end_index = len(input_list) - 1
    if linear_search(input_list, number) == rotated_array_search(input_list, start_index, end_index, number):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 2])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
