import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_number = max_number = ints[0]
    for x in ints:
        if x < min_number:
            min_number = x
        if x > max_number:
            max_number = x

    min_max = (min_number, max_number)
    return min_max


# Test cases
test_case_1 = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(test_case_1)
print("Pass" if ((0, 9) == get_min_max(test_case_1)) else "Fail")

test_case_2 = [23, 1, 22, 2, 23, 0, 1, 0]
print("Pass" if ((0, 23) == get_min_max(test_case_2)) else "Fail")

test_case_3 = [0]
print("Pass" if ((0, 0) == get_min_max(test_case_3)) else "Fail")
