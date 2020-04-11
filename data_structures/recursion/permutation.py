# Code
import copy


def permute(input_list):
    """
    Return a list of permutations

    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]

    Args:
      input_list(list): list of items to be permuted

    Returns:
      list of permutation with each permuted item being represented by a list
    """

    permutations = []

    if len(input_list) <= 1:
        permutations.append(input_list)

    else:
        first_element = input_list[0]
        after_first = slice(1, None)
        sub_permutes = permute(input_list[after_first])
        for p in sub_permutes:
            for i in range(len(p) + 1):
                r = copy.deepcopy(p)
                r.insert(i, first_element)
                permutations.append(r)

    return permutations


# Test Cases
# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.

    Note that the ordering of the list is not important.

    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list

    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input

    o.sort()
    e.sort()
    return o == e


print("Pass" if (check_output(permute([]), [[]])) else "Fail")
print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print("Pass" if (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
