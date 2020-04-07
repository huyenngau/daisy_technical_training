# check a number is prime or not
def is_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True


def prime_number_in_nth(nth):
    number = 2
    prime_index = 1

    while prime_index <= nth:
        number = number + 1
        if is_prime_number(number):
            prime_index += 1

    return number


test_number = prime_number_in_nth(10001)
print(test_number)
