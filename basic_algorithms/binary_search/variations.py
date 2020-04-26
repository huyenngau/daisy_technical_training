def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12]
print(recursive_binary_search(7, multiple))


def find_first_01(target, source):
    middle_index = (len(source) - 1) // 2
    if source[middle_index] <= target:
        for i in range(middle_index):
            if source[i] == target:
                return i
    else:
        for i in range(middle_index, len(source)):
            if source[i] == target:
                return i

    return None


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first_01(7, multiple))  # Should return 3
print(find_first_01(9, multiple))  # Should return None


def find_first_02(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None
    while source[index] == target:
        if index == 0:
            return 0
        if source[index - 1] == target:
            index -= 1
        else:
            return index


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first_02(7, multiple))  # Should return 3
print(find_first_02(9, multiple))  # Should return None


# this function that returns a boolean value indicating whether an element is _present_
def contains_01(target, source):
    index = recursive_binary_search(target, source)
    if index is not None:
        return True
    else:
        return False


letters = ['a', 'c', 'd', 'f', 'g']
print(contains_01('a', letters))  # True
print(contains_01('b', letters))  # False


# Native implementation of binary search in the `contains` function.
def contains_02(target, source):
    if len(source) == 0:
        return False
    center = (len(source) - 1) // 2
    if source[center] == target:
        return True
    elif source[center] < target:
        return contains_02(target, source[center + 1:])
    else:
        return contains_02(target, source[:center])


letters = ['a', 'c', 'd', 'f', 'g']
print(contains_02('c', letters))  # True
print(contains_02('b', letters))  # False
