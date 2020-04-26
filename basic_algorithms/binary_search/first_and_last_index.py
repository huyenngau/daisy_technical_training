def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # Note that you may want to write helper functions to find the start
    # index and the end index
    start_index = find_first_index(arr, number, 0, len(arr) - 1)
    end_index = find_end_index(arr, number, 0, len(arr) - 1)
    return [start_index, end_index]


def find_first_index(arr, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = arr[mid_index]

    if mid_element == target:
        current_index = find_first_index(arr, target, start_index, mid_index - 1)
        if current_index != -1:
            return current_index
        else:
            return mid_index
    elif target < mid_element:
        return find_first_index(arr, target, start_index, mid_index - 1)
    else:
        return find_first_index(arr, target, mid_index + 1, end_index)


def find_end_index(arr, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = arr[mid_index]

    if mid_element == target:
        current_index = find_end_index(arr, target, mid_index + 1, end_index)
        if current_index != -1:
            return current_index
        else:
            return mid_index
    elif target < mid_element:
        return find_end_index(arr, target, start_index, mid_index - 1)
    else:
        return find_end_index(arr, target, mid_index + 1, end_index)


def test_function(test_case):
    test_input_list = test_case[0]
    test_number = test_case[1]
    test_solution = test_case[2]
    test_output = first_and_last_index(test_input_list, test_number)
    if test_output == test_solution:
        print("Pass")
    else:
        print("Fail")


input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)


input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)


input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)


input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)