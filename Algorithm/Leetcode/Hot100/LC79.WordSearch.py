from typing import List

"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
解题思路：DFS+回溯
1. 我们先构建一个DFS函数，其中的参数是 i，j 分别表示棋盘上的坐标，idx 表示当前在匹配word中的第几个字符；
    * 失败的基线条件（这个最常见），要么就是下标越界，如果下标不越界就是 board[i][j] != word[idx]；
    * 成功的基线条件（我们要找的唯一状态，不常见，因此发现了True就要直接返回它），不断的匹配成功之后，word 的最后一个字符也匹配上了。
2. 我们为了回溯，需要记下我们 board[i][j] 当前的字符记为 origin，为了防止下次遍历的时候又遍历到自己，先把它改成任意别的字符，比如 '#'：
    * 从这个点出发，我们往四个方向都进行dfs，用or逻辑符连接他们，这代表着如果发现了一个True就会返回True；
    * 我们进行剪枝优化，如果发现了True就不回溯了（事实上只要True之后我们就不需要board任何事了），直接返回出来；
    * 如果不是True，说明就是False了，我们先回溯，把 '#' 改回原来的字符，并且返回 False 被上层捕获。
3. 由于存在着失败基线，我们可以对所有的字符依次用dfs方法，因为如果第一个字符匹配不上就直接返回False了。我们做一个优化，我们先找能匹配第一个字符的start点，再进行依次遍历。
* 实现细节：
为了回溯的鲁棒性，我们应该无论如何在回溯结束，就把被替换的字符复原，如下所示：
43    found = (dfs(i + 1, j, k + 1) or
44             dfs(i - 1, j, k + 1) or
45             dfs(i, j + 1, k + 1) or
46             dfs(i, j - 1, k + 1))
47    # 回溯，无论成功失败，都要把格子状态恢复，以免影响其他路径的搜索
48    board[i][j] = original_char
49    return found
这样的做法是不破坏题目原来的数组，也容易迁移到别的条件上。但是提前退出的性能更高，所以我们尽管用着剪枝的方法，还是要知道最具有鲁棒性的做法。
原来的做法：时间75.43% / 空间68.00%；提前退出的做法：时间79.58% / 空间88.09%。
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, idx: int) -> bool:
            # 失败的Baseline：下标越界（先判断）或者当前字母不等于idx的那个字母（后判断）
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != word[idx]:
                return False
            # 唯一成功的Baseline：字母全都匹配直到最后一个字符（这个True的话需要让整个判断变成True返回）
            if idx == len(word) - 1:
                return True
            # 为了防止死循环（不断上下/左右导致），我们遍历完当前字符之后把它变成一个其他符号（不是字母表中的任意）
            # 但是为了回溯，我们得记下原来是什么字母，以便改回去
            origin: str = board[i][j]
            board[i][j] = '#'
            found: bool = (dfs(i + 1, j, idx + 1) or
                           dfs(i, j + 1, idx + 1) or
                           dfs(i - 1, j, idx + 1) or
                           dfs(i, j - 1, idx + 1))
            if found:
                return True
            board[i][j] = origin
            return False

        # 开始搜寻起点在哪里出现
        start: List[tuple[int, int]] = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    start.append((i, j))
        # 如果board上面没有任何字母能够匹配word首字母，就返回False
        if not start:
            return False
        # 从起点开始找
        for i, j in start:
            if dfs(i, j, 0):
                return True
        return False
