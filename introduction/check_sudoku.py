correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


# Define a function check_sudoku() here:
def check_sudoku(square):
    for row in square:
        # create a list of expect elements
        expect_list = list(range(1, len(row) + 1))

        # check elements in each row
        for x in row:
            if x not in expect_list:
                return False
            expect_list.remove(x)

    for i in range(len(square[0])):
        expect_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[i] not in expect_list:
                return False
            expect_list.remove(row[i])

    return True


print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False
