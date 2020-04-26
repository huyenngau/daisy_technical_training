class Group(object):
    def __init__(self, name):
        self.name = name  # group name
        self.groups = []  # list of child groups
        self.users = []  # list of user_names/ids

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for group in group.get_groups():
        if is_user_in_group(user, group):
            return True
    return False


# Test cases
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child2 = Group("subchild2")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
child.add_group(sub_child2)
parent.add_group(child)


print(is_user_in_group("sub_child_user", parent))  # return True
print(is_user_in_group("sub_child_user", sub_child))  # return True
print(is_user_in_group("sub_child_user", sub_child2))  # return False
