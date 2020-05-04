def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list

    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    lower_char = []
    upper_char = []
    n = len(string)
    for i in range(n):
        if string[i].islower():
            lower_char.append(string[i])
        elif string[i].isupper():
            upper_char.append(string[i])

    # Sort the list of lower characters and upper characters
    sorted_lower_char = sorted(lower_char)
    sorted_upper_char = sorted(upper_char)

    i = 0
    j = 0
    output = ""
    for k in range(n):
        # if the character is lower-case,
        # pick lower-case character from sorted string to place in output list
        if string[k].islower():
            string[k] = sorted_lower_char[i]
            i += 1

        # pick upper-case character from sorted string to place in output list
        else:
            string[k] = sorted_upper_char[j]
            j += 1

    return output.join(string)


def test_function(test_case):
    test_string = [i for i in test_case[0]]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")


# Test cases
test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)


test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)