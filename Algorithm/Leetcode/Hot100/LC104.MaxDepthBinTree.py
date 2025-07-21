from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
解题思路：递归+二叉树遍历
我们在递归的辅助函数中融入可以记录当前深度的数组，最后返回数组的最大值即可。
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level_list: List[int] = []
        self.inorderTransverse(root, level_list, 1)
        return max(level_list)

    def inorderTransverse(self, root: Optional[TreeNode], levels: List[int], cur_level: int) -> None:
        if root:
            self.inorderTransverse(root.left, levels, cur_level + 1)
            levels.append(cur_level)
            self.inorderTransverse(root.right, levels, cur_level + 1)
