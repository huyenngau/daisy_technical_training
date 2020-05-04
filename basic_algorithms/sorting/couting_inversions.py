def count_inversions(arr):
    inversions = []
    n = len(arr)
    for i in range(n - 1):
        for j in range(1, n):
            if i < j and arr[i] > arr[j]:
                inversions.append((arr[i], arr[j]))
    return len(inversions)


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")


# Test cases
arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)


arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)


arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)