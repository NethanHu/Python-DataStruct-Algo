# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
解题思路：DFS+求公共前缀
例如如下的树结构：
                3
              /   \
            5       1
          /   \   /   \
        6     2   0    8
            /   \
           7     4
1. 我们写一个公共方法DFS，用来深度搜索树，找到我们要找的p、q两个节点，并把节点的遍历路径保存下来。比如我们要找0和4的公共祖先：
    * 找到0的时候，路径为 [3, 1, 0]
    * 找到4的时候，路径为 [3, 5, 2, 4]
    * 最后我们使用zip函数（zip函数只会使两份长度不一的数组变成((3, 3), (1, 5), (0, 2))的格式），我们只取i和j相等的作为祖先。
2. 我们在实现的时候有几个小细节：
    * 我们在path_to_node进行append的时候，一定是path的快照，不能是path的引用，否则在后面的回溯中会错误；
    * 一定要记得回溯，即当前的节点遍历完了之后，需要从path中pop掉，否则就是一整个前序遍历的结果，不能只获得当前路径。
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_to_node: List[List[TreeNode]] = []

        def dfs(cur: Optional[TreeNode], path: List[TreeNode], node: TreeNode) -> None:
            if cur:
                path.append(cur)
                if cur is node:
                    # 这边要存储path的快照，不能直接append path，否则引用的变化会导致出现问题
                    path_to_node.append(path[:])
                    return
                dfs(cur.left, path, node)
                dfs(cur.right, path, node)
                # 回溯的逻辑：这个点遍历完了，要出去的时候记得把自己pop出去
                path.pop()

        dfs(root, [root], p)
        dfs(root, [root], q)

        ancestor: Optional[TreeNode] = None
        path_to_p: List[TreeNode] = path_to_node[0]
        path_to_q: List[TreeNode] = path_to_node[1]
        for i, j in zip(path_to_p, path_to_q):
            if i is j:
                ancestor = i
            else:
                break
        return ancestor
