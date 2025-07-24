# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
有效 二叉搜索树定义如下：
节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
解题思路：递归+有效区间传递 或者 中序遍历
1. 先讲中序遍历，会用到中序遍历的特性：一个有效的二叉搜索树，它的中序遍历结果必然是一个严格递增的序列。
2. 我们再说递归+有效区间传递。这里我之前犯了一个常见误区，对于以下的二叉树：
        5
       / \
      4   6
         / \
        3   7
    * 如果只判断当前元素是否大于左边，小于右边，会导致算法仅限于局部，看不到全局（比如右边的3小于5，不满足BST）；
    * 因此我们在递归传参的时候需要加上一定的限制；
    * 对于当前元素node，我们需要保证它的左子树中的所有元素都小于node.val，而且不能相等，因此 low < node.left.val < node.val 是必要条件；
    * 当进入到node.left的时候，根据递归的传递性，对于一个有效的BST，node.left.left也得满足该条件 low < node.left.left.val < node.left.val；
    * 随着递归越来越深入，high这个边界会不断变小，约束力不断变强。对于右子树同理。
3. 我们在isValidBST方法中写recValidate的目的是为了让递归函数变成private，将它“藏”在 isValidBST 内部是更好的封装；同时不再需要写self。
"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def recValidate(node: Optional[TreeNode], low=-math.inf, high=math.inf) -> bool:
            # 如果一边没有子节点，就不需要比较并且返回安全的True
            if not node:
                return True
            if not low < node.val < high:
                return False
            return recValidate(node.left, low, node.val) and recValidate(node.right, node.val, high)

        return recValidate(root)