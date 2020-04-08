# check a number is prime or not
def is_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def prime_number_in_nth(nth):
    number = 2
    prime_index = 1
    import time
    start_time = time.time()
    while prime_index <= nth:
        number = number + 1
        if is_prime_number(number):
            prime_index += 1

    end_time = time.time()
    print(end_time - start_time)
    return number


# bool_value = is_prime_number(9)
# print(bool_value)

test_number = prime_number_in_nth(10001)
print(test_number)
