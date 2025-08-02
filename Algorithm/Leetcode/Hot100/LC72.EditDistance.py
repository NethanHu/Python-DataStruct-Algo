from typing import List

"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数。
你可以对一个单词进行如下三种操作：插入一个字符、删除一个字符、替换一个字符。
思路分析：线性规划。这道题目是线性规划的集大成题目，涉及到的状态转移也是非常的巧妙。
1. 设想一下在 word1 中有指针 i、word2 中有指针 j（它们还不是DP数组中的i、j），我们依次比较 word1[i] 和 word2[j]：
    * 假设它们是相同的，此时不用做任何操作（步骤+0）。那么目前总的操作数就由判断 word1、word2 的上一个字母的结果继承下来；
    * 假设它们不同，如何把它们变得相同呢？
        - 要么删除 word1 中第 i 个字符，那么此时就由 i - 1 元素去负责比较了，然后这时候寻找上一步骤（不由自己处理，只要状态转移过来），因为删除了元素，此时操作数 dp[i - 1][j] + 1；
        - 要么删除 word2 中第 j 个字符，那么此时就由 j - 1 元素去负责比较了，那么操作数 dp[i][j - 1] + 1；
        - 要么添加一个元素，此时有个有趣的等式关系：word2添加一个元素，相当于word1删除一个元素，例如 word1 = "ad" ，word2 = "a"，word1删除元素'd' 
        和 word2 添加一个元素'd'，变成 word1="a", word2="ad"，最终的操作数是一样；
        - 要么就把当前不一样的元素改成相同，此时不涉及到要变成上一元素，当前的操作数就是 dp[r - 1][c - 1] + 1。
2. 初始化

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]
        # 初始化第一行和第一列，都是 +1 递增，表示一个完整字符串如何逐步变成空
        for c in range(n + 1):
            dp[0][c] = c
        for r in range(m + 1):
            dp[r][0] = r
        # 逐步开始填表，分成两大类：相等或者不等（增删改）
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(dp[r - 1][c] + 1, dp[r][c - 1] + 1, dp[r - 1][c - 1] + 1)
        return dp[-1][-1]
