from collections import deque
from typing import Optional, List, Deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
解题思路：BFS，但是可以优化
1. 我们主要的思路是基于BFS，但是我们从右边开始加入元素，因此BFS实际上是从右往左；
2. 我们做了个优化，如果右边已经有了元素，那么就不再进行填充其左边的别的元素，直接continue接下来的操作。
"""


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level_nums: List[List[int]] = []
        queue: Deque[TreeNode] = deque([root])
        while queue:
            cur_level: List[int] = []
            for _ in range(len(queue)):
                node: TreeNode = queue.popleft()
                cur_level.append(node.val)
                # 因为我们需要的是右视图，所以每次填充一层节点的时候我们从右边开始
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                # 我们可以这里做个优化条件，如果这一层已经有右边看到的一个元素，那么该元素左边别的都不需要考虑
                if cur_level:
                    continue
            level_nums.append(cur_level)
        ans: List[int] = []
        for level in level_nums:
            ans.append(level[-1])
        return ans
