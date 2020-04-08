def swap(x, y):
    tmp = x
    x = y
    y = tmp
    return x, y


def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    if len(input) == 0:
        return input
    else:
        return reverse_string(input[1:]) + input[0]


print(reverse_string("abc"))


# Test Cases
print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")