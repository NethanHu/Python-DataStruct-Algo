from Tree.BinarySearchTree import BinarySearchTree, TreeNode


class AVLTreeNode(TreeNode):
    def __init__(self, key, val, left=None, right=None, parent=None):
        super().__init__(key, val)
        self.left_child: AVLTreeNode | None = left
        self.right_child: AVLTreeNode | None = right
        self.parent: AVLTreeNode | None = parent
        self.balance_factor = 0


# AVL树的实现，大部分与BST相似，我们主要关心几个方法
class AVLTree(BinarySearchTree):
    def rotate_left(self, rot_root: AVLTreeNode):
        new_root: AVLTreeNode = rot_root.right_child
        rot_root.right_child = new_root.left_child
        if new_root.left_child is not None:
            new_root.left_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root
        new_root.left_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        rot_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)

    def rotate_right(self, rot_root: AVLTreeNode):
        new_root: AVLTreeNode = rot_root.left_child
        rot_root.left_child = new_root.right_child
        if new_root.right_child:
            new_root.right_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right_child():
                rot_root.parent.right_child = new_root
            else:
                rot_root.parent.left_child = new_root
        new_root.right_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(rot_root.balance_factor, 0)

    def rebalance(self, node: AVLTreeNode):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)

    def update_balance(self, node: AVLTreeNode):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def _put(self, key, val, cur_node: AVLTreeNode):
        if key < cur_node.key:
            if cur_node.has_left_child():
                self._put(key, val, cur_node.left_child)
            else:
                cur_node.left_child = AVLTreeNode(key, val, parent=cur_node)
                self.update_balance(cur_node.left_child)
        else:
            if cur_node.has_right_child():
                self._put(key, val, cur_node.right_child)
            else:
                cur_node.right_child = AVLTreeNode(key, val, parent=cur_node)
                self.update_balance(cur_node.right_child)