def even_fibonacci_numbers(first=1, second=2):
    term = 0
    sum_even_term = 2
    while term < 4000000:
        term = first + second
        if term >= 4000000:
            break

        first = second
        second = term

        if term % 2 == 0:
            sum_even_term += term
    return sum_even_term


sum = even_fibonacci_numbers()
print(sum)
