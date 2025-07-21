from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给你一个二叉树的根节点 root ，检查它是否轴对称。
解题思路：前序遍历+后序遍历
1. 我们观察对称数的样子，很明显是以根节点为法线，左右两个子树的相互对称；
2. 我们可以把这两个子树分别进行前序遍历和后序遍历（实际上这也模拟了找对称节点的过程），把val填充进数组中；
    * 在这里我们如果碰到了None节点，必须把None也填充进数组里面，因为如果只填充数字节点，那么Case2就是一个反例
3. 最后我们比较一下由两个子树生成的数组是否一一相等即可。
"""


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l_nums: List[Optional[int]] = []
        r_nums: List[Optional[int]] = []
        self.preorderTraversal(root.left, l_nums)
        self.postorderTraversal(root.right, r_nums)
        return l_nums == r_nums

    def preorderTraversal(self, root: Optional[TreeNode], num_list: List[Optional[int]]):
        if root:
            num_list.append(root.val)
            self.preorderTraversal(root.left, num_list)
            self.preorderTraversal(root.right, num_list)
        else:
            num_list.append(None)

    def postorderTraversal(self, root: Optional[TreeNode], num_list: List[Optional[int]]):
        if root:
            num_list.append(root.val)
            self.postorderTraversal(root.right, num_list)
            self.postorderTraversal(root.left, num_list)
        else:
            num_list.append(None)
