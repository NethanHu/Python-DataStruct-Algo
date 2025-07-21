from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
解题思路：递归+前序遍历
这里经过测试，必须使用前序或者后序遍历（不能使用中序遍历）。否则会翻转两次=没有翻转。
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.preorderTransversal(root)
        return root


    def preorderTransversal(self, root: Optional[TreeNode]) -> None:
        if root:
            root.left, root.right = root.right, root.left
            self.preorderTransversal(root.left)
            self.preorderTransversal(root.right)
