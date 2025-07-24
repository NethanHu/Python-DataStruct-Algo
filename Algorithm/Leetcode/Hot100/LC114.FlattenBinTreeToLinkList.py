# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 前序遍历 顺序相同。
思路分析：DFS+头插法
1. 我们先记住，递归的顺序是向右、向左，然后处理自身
    * 为什么向右呢？结合上一题LC199，我们处理这种右边「这一侧」问题的时候都取先向右。或者这样理解，对于新的一条树，只有第一位和最后的元素和一开始是一样的，
      中间所有的元素都重新经过了链接。因此我们从右下不断往左上进行处理；
    * 对于所有的子问题，我们进行一个递推：
        - 当前节点是root，先把它自己的左子树置空（不要担心会丢失左子树信息，因为DFS能保证所有的节点都会经过遍历）；
        - 然后我们使用一个临时节点head，来表示当前已经变成「一条树」的这群节点的头节点，把这「一条树」挂在当前节点的右边；
        - 最后把head上移一格。
2. 思路比较绕，可以多加复习。
"""


class Solution:
    head: Optional[TreeNode] = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left = None
        root.right = self.head
        self.head = root
