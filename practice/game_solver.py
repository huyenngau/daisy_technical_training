def game_solver(square):
    if solver(square):
        for row in square:
            print(row)

        print("-- Successfully! --" + "\n")
    else:
        print("Error! Please input square with size n×n, n >= 4, and n is even number.")


def solver(square):
    n = len(square[0])
    x = 0
    y = 0
    flag = False
    # Find cells that haven't been colored
    for x in range(n):
        for y in range(n):
            if square[x][y] == 0:
                flag = True
                break
        if flag:
            break

    # if no more cells are not colored => completed
    if flag is False:
        return True

    # If assign 1 is safe
    square[x][y] = 1
    if is_safe(square, x, y, 1):
        # solve the next cells in the square
        if solver(square):
            return True

    # If assign 2 is safe
    square[x][y] = 2
    if is_safe(square, x, y, 2):
        # solve the next cells in the square
        if solver(square):
            return True

    square[x][y] = 0
    return False


"""
Conditions: 
1. No three consecutive tiles have the same colour.
2. On each row or column of the grid, the number of red tiles equals to the number of blue ones.
3. No two rows or no two columns are the same.
"""


def is_safe(square, x, y, value):
    n = len(square[0])

    if x - 2 > 0:
        left = x - 2
    else:
        left = 0
    if x >= n - 2:
        right = n - 3
    else:
        right = x

    # check 3 different cells in a row
    for i in range(left, right + 1):
        if square[i][y] == value and square[i + 1][y] == value and square[i + 2][y] == value:
            return False

    if y - 2 > 0:
        left = y - 2
    else:
        left = 0
    if y >= n - 2:
        right = n - 3
    else:
        right = y

    # check 3 different cells in a column
    for j in range(left, right + 1):
        if square[x][j] == value and square[x][j + 1] == value and square[x][j + 2] == value:
            return False

    # check row/column is filled out completed or not
    require_check_row = True
    require_check_column = True
    for i in range(n):
        if square[x][i] == 0:
            require_check_row = False

    for i in range(n):
        if square[i][y] == 0:
            require_check_column = False

    # check the number of red tiles equals to the number of blue ones in a row
    if require_check_row:
        sum_row = 0
        for i in range(n):
            sum_row += square[x][i]
        if sum_row != n * 3 / 2:
            return False

        for i in range(n):
            if i != x:
                if compare_row(square, i, x):
                    return False

    # check the number of red tiles equals to the number of blue ones in a column
    if require_check_column:
        sum_column = 0
        for i in range(n):
            sum_column += square[i][y]
        if sum_column != n * 3 / 2:
            return False

        for i in range(n):
            if i != y:
                if compare_column(square, i, y):
                    return False

    # If safe return True
    return True


def compare_row(square, i, j):
    for k in range(0, len(square)):
        if square[i][k] != square[j][k]:
            return False
    return True


def compare_column(square, i, j):
    for k in range(0, len(square)):
        if square[k][i] != square[k][j]:
            return False
    return True


input_1 = [
    [1, 1, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 2],
    [0, 0, 1, 0],
]

input_2 = [
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 2, 0]
]

input_3 = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 2, 0, 0, 0],
    [0, 0, 0, 0, 2],
]

print("Test case 1: " + "\n")
game_solver(input_1)

print("Test case 2: " + "\n")
game_solver(input_2)

print("Test case 3: " + "\n")
game_solver(input_3)
