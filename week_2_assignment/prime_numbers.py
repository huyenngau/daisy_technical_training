def is_prime_number(number):
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            return False
        factor += 1
    return True


def prime_number_in_nth(nth):
    if nth == 1:
        return 2

    number = 1
    prime_index = 1

    while prime_index < nth:
        number += 2
        if is_prime_number(number):
            prime_index += 1

    return number


# Test
test_number = prime_number_in_nth(10001)
print(test_number)
