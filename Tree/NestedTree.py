def BinaryTree(r):
    return [r, [], []]

def insert_left(root: list, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root: list, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root: list):
    return root[0]

def set_root_val(root: list, new_val):
    root[0] = new_val

def get_left_child(root: list):
    return root[1]

def get_right_child(root: list):
    return root[2]