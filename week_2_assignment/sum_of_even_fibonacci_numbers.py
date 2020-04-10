def sum_of_even_fibonacci_numbers(max_fibonacci_number):
    if max_fibonacci_number < 2:
        return 0

    first_fibonacci_number = 1
    second_fibonacci_number = 2
    fibonacci_number = 0
    sum_even_term = 2
    while fibonacci_number < max_fibonacci_number:
        fibonacci_number = first_fibonacci_number + second_fibonacci_number

        first_fibonacci_number = second_fibonacci_number
        second_fibonacci_number = fibonacci_number

        if fibonacci_number % 2 == 0:
            sum_even_term += fibonacci_number
    return sum_even_term


# Test
test_result = sum_of_even_fibonacci_numbers(4000000)
print(test_result)
