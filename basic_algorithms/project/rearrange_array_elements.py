def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_input_list = mergesort(input_list)

    n = len(sorted_input_list)

    # The first number is filled with digits at the even indices of the sorted input list
    x = 0
    for i in sorted_input_list[slice(0, n, 2)]:
        print(i)
        x = x * 10 + i

    # The second number is filled with digits at the odd indices of the sorted input list
    y = 0
    for k in sorted_input_list[slice(1, n, 2)]:
        y = y * 10 + k

    return x, y


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_case_1 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case_1)

test_case_2 = [[1, 2, 3, 4, 5], [531, 42]]
test_function(test_case_2)

test_case_3 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case_3)
