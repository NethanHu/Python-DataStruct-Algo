from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。
思路分析：中序遍历
1. 由于BST的特性，中序遍历（前+root+后）的遍历方法返回的结果就是排序之后的元素；
2. 所以现在的问题在于，我们如何在中序遍历过程中某一步停下返回结果。根据BST性质，我们只要记录下中序遍历获得了几个节点，在第K的时候停下即可；
3. 最后我们把记录结果中的第K个元素返回即可。
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num_record: List[int] = []
        self.inorderTraversal(root, num_record, k)
        return num_record[k - 1]


    def inorderTraversal(self, root: Optional[TreeNode], record: List[int], k: int) -> None:
        if root:
            self.inorderTraversal(root.left, record, k)
            record.append(root.val)
            # 这边使用 >= 会比 == 时间更优，因为这算是一个中途退出条件，如果已经有了第K个元素，后续不再需要进行操作
            if len(record) >= k:
                return
            self.inorderTraversal(root.right, record, k)
