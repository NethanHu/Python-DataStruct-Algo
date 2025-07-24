from collections import defaultdict, deque
from typing import Optional, List, Deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
给你二叉树的根节点 root ，返回其节点值的层序遍历。（即逐层地，从左到右访问所有节点）。
解题思路：直接使用BFS 或者 DFS+递归
1. DFS+递归在这里不是解题重点，此题目更要求我们掌握BFS的方法，因此注释掉DFS方法。
2. BFS是标准的解题思路，使用BFS需要实现以下几点功能：
    * 判断特殊情况，如果root为空，那么直接返回空数组即可；
    * 使用一个deque来表示队列，新发现的node添加在后面，需要拿出node遍历的时候从前面弹出；
    * 总的循环结束条件是queue为空；在queue不为空的时候，我们就对queue中的node进行一一遍历（此时这些node都在同一层）；
    * 尽管node会不断在queue后面加入，我们只需要打个checkpoint，只需要遍历一开始queue中的node个数；
    * 如果node有左子节点、右子节点，就在queue中append，对于本题从左到右的遍历，我们先append左子节点然后再append右子节点。
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans: List[List[int]] = []
        queue: Deque[TreeNode] = deque([root])
        while queue:
            vals: List[int] = []
            # 在当前层做一个checkpoint，只遍历当前层数数量的nodes
            for _ in range(len(queue)):
                node: TreeNode = queue.popleft()
                vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(vals)
        return ans



    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     node_dict: dict[int, List[int]] = defaultdict(list)
    #     ans: List[List[int]] = []
    #     self.preorderTraversal(root, node_dict, 1)
    #     for level in node_dict.keys():
    #         ans.append(node_dict[level])
    #     return ans
    #
    #
    # def preorderTraversal(self, root: Optional[TreeNode], node_dict: dict[int, List[int]], level: int) -> None:
    #     if root:
    #         node_dict[level].append(root.val)
    #         self.preorderTraversal(root.left, node_dict, level + 1)
    #         self.preorderTraversal(root.right, node_dict, level + 1)