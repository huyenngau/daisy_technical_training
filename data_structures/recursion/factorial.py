def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n == 0:
        return 1
    else:
        output = n * factorial(n-1)
    return output


print(factorial(4))

# Test Cases
print("Pass" if (1 == factorial(0)) else "Fail")
print("Pass" if (1 == factorial(1)) else "Fail")
print("Pass" if (120 == factorial(5)) else "Fail")
