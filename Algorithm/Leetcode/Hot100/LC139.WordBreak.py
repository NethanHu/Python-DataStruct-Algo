from typing import List

"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
解题思路：记忆化搜索+深度优先搜索
1. 这道题目逃不开需要对字符串的遍历，但是我们在这基础上可以做很多优化；首先是我们可以把 wordDict 变成 set，这样的哈希表有助于我们在 O(1) 的时间内进行搜索；
2. 我们设计一个 DFS 的方法，我们把字符串分成「前+后」两个子串，同时设置一个从后往前遍历的指针 i，通过这个指针，我们把字符串变成了 [:i + 1] 和 [i + 1:]两部分：
    * 同时基于 i 这个点，我们设置一个指针 j 从后往前遍历（最长的遍历距离等于 wordDict 中最长的单词长度），截取 s[j: i] 这段字符串，拿来和哈希表中的单词进行匹配：
        - 如果我们发现 s[j: i] 这个子串是哈希表中的单词，那么从 j 点出发，我们进行新一波搜索；
        - 什么时候 j 的位置能到 0，就说明之前所有的子串都可以对应哈希表中的一个单词，那么此时说明搜索成功，返回 True；
        - 我们采取记忆化搜索，Python 里面可以直接使用 function 的注解 @cache，能够使用 LRU 缓存记录该函数历史上的「参数+输出」组合，
          意思是，假设历史上有过在 i == 5 的时候返回 True，那么接下来再次碰到 dfs(5) 的时候会直接返回 True，不会再进行搜索。
    举例：
                                i
                                ↓
    c   a   t   s   a   n   d   o   g
                    ↑
                    j（从i出发往左移动）
    此时 s[j: i] 就是 'and'，然后我们查询哈希表中是否存在 'and' 这个单词。如果存在，那么此时 i 就变成了 j 所在的位置。新的 j 从 i 出发再次一路向前深度搜索。
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len: int = max([len(word) for word in wordDict])
        words: set[str] = set(wordDict)

        def dfs(i: int) -> bool:
            if i == 0:
                return True
            # 这边我们采用 max(i - max_len - 1, -1) 的原因是：可能从 i 出发往前不足以完成一整个 max_len 的搜索，因此这时的搜索最多到索引为 0 处
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if s[j: i] in words and dfs(j):
                    return True
            return False

        return dfs(len(s))
