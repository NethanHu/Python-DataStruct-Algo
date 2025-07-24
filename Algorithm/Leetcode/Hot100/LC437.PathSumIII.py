# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
解题思路：找路径问题用「DFS」 + 求连续的和用「前缀和」
1. 首先我们先复习一下前缀和的知识：
    * 我们创建一个前缀和的表，初始元素只有一个0（表示得到和为0存在一个做法，即什么都不选），然后创建一个cur_sum逐渐累加所有元素，不断append到前缀和prefix中；
    * 对于给定一个target，我们已经获取到了当前元素的前缀和cur_sum，如何判断是否有连续元素的和等于target呢？我们只要查找cur_sum-target是否在prefix中即可；
    * 对于我们使用的defaultdict，如果不存在key就返回0，因此我们每次就不需要进行查找，直接count += prefix[cur_sum - target]，如果存在就会加一个正数。
2. 我们接下来使用DFS来获取到从根节点到当前节点的路径，并且传递一个cur_sum来累加，并且使用一个全局哈希表来存储前缀和；
3. 我们再结合递归回溯的优良特性：每一层都有自己的cur_sum，且和后面的状态互不干扰；如果遍历完自己这个节点之后，就可以直接把自己的cur_sum从哈希表中删除。
4. 方法很巧妙，建议背下来。
"""


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        prefix: dict[int, int] = defaultdict(int)
        # 一个常规的前缀和初始化技巧
        prefix[0] = 1
        count: int = 0
        target: int = targetSum

        def dfs(node: Optional[TreeNode], cur_sum: int) -> None:
            if not node:
                return
            cur_sum += node.val
            nonlocal count
            # 前缀和的巧妙之处在于：只会找「当前遍历到的元素」是否和其前面连续几个数和等于target，
            # 而非找整个表中连续的某个部分，这样就不会重复找
            count += prefix[cur_sum - target]
            prefix[cur_sum] += 1
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            # 同时另一个巧妙之处在于，递归会在每一层存储一份自己的状态，比如cur_sum，这样找完了这个节点回溯的时候可以马上删除自己
            prefix[cur_sum] -= 1

        dfs(root, 0)
        return count
