# check a number is prime or not
def is_prime_number(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def prime_number_in_nth(nth):
    if nth == 1:
        return 2

    number = 2
    prime_index = 1

    while prime_index < nth:
        number = number + 1
        if is_prime_number(number):
            prime_index += 1
        if prime_index == nth:
            return number

    return None


# Test
test_number = prime_number_in_nth(10001)
print(test_number)
