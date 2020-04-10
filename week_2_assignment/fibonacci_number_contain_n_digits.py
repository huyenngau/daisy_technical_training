def index_of_first_fibonacci_number_contain_n_digits(number_of_digits):
    if number_of_digits < 1:
        return None

    if number_of_digits == 1:
        return 1

    first_fibonacci_number = 1
    second_fibonacci_number = 1
    index = 2

    while True:
        fibonacci_number = first_fibonacci_number + second_fibonacci_number\

        first_fibonacci_number = second_fibonacci_number
        second_fibonacci_number = fibonacci_number
        index += 1

        if fibonacci_number / (10**(number_of_digits-1)) > 1:
            return index


# Test
index_test_result = index_of_first_fibonacci_number_contain_n_digits(1000)
print(index_test_result)
