from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给你一棵二叉树的根节点，返回该树的 直径 。
二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
两节点之间路径的 长度 由它们之间边数表示。
解题思路：DFS
1. 对于每个节点，我们可以通过DFS求得它左子树、右子树的最大深度；那么对于这个节点来说，直径等于两边的最大深度之和；
2. 思路借鉴于灵神，我们构造一个可以求得左右子树深度的函数dfs：
    * 我们为了记忆化，使用一个数组d_list来保存当前节点的直径；
    * 对于每一个节点node，我们分别两边遍历左子节点和右子节点，每次dfs一次，都把任务分解给自己的子节点去完成，然后获取到子节点传回来的长度+1；
    * 如果这个节点没有子节点（叶节点），为了抵消我们无论如何都加上的1，我们返回-1即可，就说明叶节点的l_len和r_len都是0；
    * 如果一个节点既有左子节点和右子节点，那么这个节点的最深距离就是两者取max；这就说明子任务结束的返回值就是该节点两边的最大深度；
    * 在其中不要忘了向d_list中去填充两者之和l_len + r_len，我们最后返回的就是d_list中的最大值。
3. 写法可以参照灵神使用nonlocal变量，但是个人认为自己实现自己熟悉的方法更方便记忆。
"""


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d_list: List[int] = []
        self.dfs(root, d_list)
        return max(d_list)

    def dfs(self, root: Optional[TreeNode], d_list: List[int]) -> int:
        if not root:
            return -1
        l_len: int = self.dfs(root.left, d_list) + 1
        r_len: int = self.dfs(root.right, d_list) + 1
        d_list.append(l_len + r_len)
        return max(l_len, r_len)
