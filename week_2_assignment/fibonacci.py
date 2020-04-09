def index_of_first_fibonacci_number_contain_n_digits(n):
    number_of_digits = 0
    f1 = 1
    f2 = 1
    index = 2
    if n == 1:
        return 1
    while number_of_digits < n:
        fibonacci_number = f1 + f2
        f1 = f2
        f2 = fibonacci_number
        index += 1
        if fibonacci_number / (10**(n-1)) > 1:
            return index


index = index_of_first_fibonacci_number_contain_n_digits(1000)
print(index)