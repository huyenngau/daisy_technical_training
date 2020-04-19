import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    list_of_files = os.listdir(path)
    list_of_paths = list()

    for f in list_of_files:
        new_path = os.path.join(path, f)
        if os.path.isdir(new_path):
            list_of_paths += find_files(suffix, new_path)
        else:
            if new_path.endswith(suffix):
                list_of_paths.append(new_path)

    return list_of_paths


# Test case
print(find_files(".c", path="./file_recursion"))
print(find_files(".c", path="./file_recursion/testdir"))
print(find_files(".h", path="./file_recursion/testdir"))
