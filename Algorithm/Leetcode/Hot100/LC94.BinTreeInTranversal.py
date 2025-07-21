from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
解题思路：二叉树递归遍历
直接构造一个辅助的递归函数，用来递归填充ans_list
"""


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans_list: List[int] = []
        self.recurInfixTrav(root, ans_list)
        return ans_list

    def recurInfixTrav(self, root: Optional[TreeNode], ans: List[int]) -> None:
        if root:
            self.recurInfixTrav(root.left, ans)
            ans.append(root.val)
            self.recurInfixTrav(root.right, ans)
