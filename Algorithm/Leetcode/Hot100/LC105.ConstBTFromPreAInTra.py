# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
解题思路：递归和分治思想
1. 我们举个例子：
            3
          /   \
         9    20
       /  \  /  \
      6   8 15   7
    * 前序遍历的结果是 [3, 9, 6, 8, 20, 15, 7]
    * 中序遍历的结果是 [6, 9, 8, 3, 15, 20, 7]
    * 根据我们对前序遍历流程的了解，我们知道preorder第一个元素就是整个树的根节点，而整个树的根节点刚好是inorder最中间那个分界点元素
2. 那么我们根据index方法得到根节点3在中序遍历中的位置 l_size=inorder.index(preorder[0])，从而得到根节点左子树和右子树分别的大小：
    * 除去3之后，左子树的前序遍历结果 [9, 6, 8]（因为左边的大小就是l_size），中序遍历结果是 [6, 9, 8]。右子树就是之后的另外三个元素；
    * 我们可以发现，左子树的第一个元素又恰好是前序遍历的根节点，我们继续可以分治，一直到前序遍历的结果是空，说明是叶节点了不再具有子树。
3. 我们在这里可以不断获取到l_size，然后用其作为分界线去对数组进行切片操作，最后递归着把整个树拼起来。
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        l_size: int = inorder.index(preorder[0])
        l_tree: Optional[TreeNode] = self.buildTree(preorder[1:1 + l_size], inorder[:l_size])
        r_tree: Optional[TreeNode] = self.buildTree(preorder[1 + l_size:], inorder[1 + l_size:])
        return TreeNode(preorder[0], l_tree, r_tree)
