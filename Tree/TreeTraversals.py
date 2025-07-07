from Tree.LinkedTree import BinaryTree


def preorder_traversal(tree: BinaryTree):
    if tree:
        print(tree.get_root_val())
        preorder_traversal(tree.get_left_child())
        preorder_traversal(tree.get_right_child())

def inorder_traversal(tree: BinaryTree):
    if tree is not None:
        preorder_traversal(tree.get_left_child())
        print(tree.get_root_val())
        preorder_traversal(tree.get_right_child())

def postorder_traversal(tree: BinaryTree):
    if tree is not None:
        preorder_traversal(tree.get_left_child())
        preorder_traversal(tree.get_right_child())
        print(tree.get_root_val())