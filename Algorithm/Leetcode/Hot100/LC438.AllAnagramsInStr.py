"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
"""
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_set: set[str] = set(p)
        p_counts: dict[str, int] = Counter(p)
        p_len: int = len(p)
        ans: List[int] = []
        for i in range(len(s) - p_len + 1):
            substr: str = s[i: i + p_len]
            if set(substr) == p_set and Counter(substr) == p_counts:
                ans.append(i)
        return ans