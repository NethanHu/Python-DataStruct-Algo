# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。
解题思路：递归+分治思想
1. 如果我们想形成一个平衡二叉树，那么任意节点的左右子树的高度差都不应超过1，所以我们就使用nums最中间那个数字，把数组一分为二，左右两边各形成新的子树；
2. 左右两边其实干的是同一件事情，只不过此时的数组变成了局部；我们可以继续把这个问题进行分治，直到数组中没有任何元素，此时返回的是None：
3. 我们使用「二分查找」的思路找到最中间那个元素，以及获取中间元素两边的新数组。
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
       if not nums:
           return None
       m: int = len(nums) // 2
       root: Optional[TreeNode] = TreeNode(nums[m])
       root.left = self.sortedArrayToBST(nums[:m])
       root.right = self.sortedArrayToBST(nums[m + 1:])
       return root
