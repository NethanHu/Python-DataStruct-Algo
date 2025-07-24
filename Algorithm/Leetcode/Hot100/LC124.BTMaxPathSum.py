# Definition for a binary tree node.
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和 。
解题思路：DFS+递归逻辑
1. 对于找路径的问题，我们首先想到的是DFS；由于我们求的是总和，因此退出条件是node为空，返回为0；DFS的逻辑如下：
    * 如果当前节点为空，意思是选不了这个节点，因此返回0，上一层+0；
    * 我们对该节点的左右两个子节点继续递归使用dfs；
    * 既然求的是路径总和最大，当下层递归结束以后会返回一个值，我们就获取到了从该节点出发能获取到的路径最大值 max(l_val, r_val) + node.val；
    * 注意有节点是负值，有可能在加上之后会导致小于零；既然会小于零，那我们干脆就不选这条路径了，不选的代价就是返回0；
    * 那么如果所有点都是负值呢？哪一条路径都不选（因为累加返回而），DFS退化为从所有的节点中找一个绝对值最小的负数，符合条件。
2. 更新答案的逻辑：
    * DFS可以帮我们一条路从上走到下，但是由于题目有要求，可以在某个点同时加上自己的左右两个节点（该点可以「拐弯」）；
    * DFS可以帮我们遍历到每一个点，因此我们可以每到一个点就进行假设，假设这个点是「拐弯点」，那么ans值就应该与l_val + r_val + node.val进行比较和更新。
3. 题目如果没刷过很难第一次想出来。这道题不复杂，但是是之前的DFS、递归本质、路径和的集大成思路。建议记住。
"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l_val: int = dfs(node.left)
            r_val: int = dfs(node.right)
            nonlocal ans
            ans = max(ans, l_val + r_val + node.val)
            return max(max(l_val, r_val) + node.val, 0)

        dfs(root)
        return int(ans)
