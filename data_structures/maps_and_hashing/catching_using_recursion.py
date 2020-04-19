def staircase(n):
    # Base Case - minimum steps possible and number of ways the child can climb them

    if n == 1:
        return 1

    # Inductive Hypothesis - ways to climb rest of the steps
    elif n == 2:
        return 2

    elif n == 3:
        return 4

    # Inductive Step - use Inductive Hypothesis to formulate a solution
    else:
        return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case = [4, 7]
test_function(test_case)

test_case = [5, 13]
test_function(test_case)

test_case = [3, 4]
test_function(test_case)

test_case = [20, 121415]
test_function(test_case)
