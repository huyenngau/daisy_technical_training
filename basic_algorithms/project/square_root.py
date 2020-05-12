def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number

    start = 1
    end = number
    while start <= end:
        mid = (start + end) // 2

        if mid ** 2 <= number:
            return mid
        else:
            end = end - 1


# Test case
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (3 == sqrt(11)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
