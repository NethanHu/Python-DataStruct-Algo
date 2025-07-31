from typing import List

"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
解题思路：栈
1. 本题正常解法是动态规划，但是逃课做法是使用栈，具体思路如下：
    * 我们创建一个标记的数组 tmp，其中 0 表示一个「中断」，连续的 1 表示连续的合法括号组；
    * 使用 stack 来填入括号下标，如果碰到 '(' 就直接填入，碰到 ')' 时如果 stack 不为空，说明有一个 '(' 与之配对，就 pop 出上一个 '(' 的下标，tmp 中把它们双双设置为 1；
    * 最后我们遍历数组，找出最长的连续 1 区间即可。
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack: List[int] = []
        n = len(s)
        tmp: List[int] = [0] * n
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    j: int = stack.pop()
                    tmp[i], tmp[j] = 1, 1
        max_len, cur_len = 0, 0
        for t in tmp:
            if t == 1:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
        return max_len
